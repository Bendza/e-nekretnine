import scrapy
import re
from ad_scraper.website_configs import WEBSITE_CONFIGS
from urllib.parse import urljoin
from datetime import datetime

class AdsSpider(scrapy.Spider):
    name = 'ads_spider'
    total_requests = sum(start_url_config['max_pages'] for config in WEBSITE_CONFIGS.values() for start_url_config in config['start_urls'])
    processed_requests = 0
    total_items = 0 

    def start_requests(self):
            for website, config in WEBSITE_CONFIGS.items():
                self.current_website = website
                for start_url_config in config['start_urls']:
                    base_url = start_url_config['url']
                    pagination_pattern = config.get('pagination_pattern', '?page={page_number}')
                    for page in range(1, start_url_config['max_pages'] + 1):
                        offset = (page - 1) * 20
                        url = f"{base_url}{pagination_pattern.format(page_number=page, offset=offset)}"
                        adType, objectType = self.get_types_from_url(url)  # getting the types from URL
                        yield scrapy.Request(url, callback=self.parse, meta={'config': config, 'website': website, 'adType': adType, 'objectType': objectType})

    def parse(self, response):
        config = response.meta.get('config')
        website = response.meta.get('website')
        ads = response.xpath(config['ad_selector'])

        adType = response.meta.get('adType')
        objectType = response.meta.get('objectType')

        for ad in ads:
            ad_data = {}
            for field, selector in config['fields'].items():
                extracted_data = ad.xpath(selector).get()
                # Process the extracted_data based on the field type
                if field in ['price']:
                    ad_data[field] = self.parse_price(extracted_data)
                elif field in ['surface']:
                    ad_data[field] = self.parse_surface(extracted_data);
                elif field in ['title', 'street']:
                    ad_data[field] = self.parse_string(extracted_data).strip()
                elif field == 'date':
                    ad_data[field] = self.parse_date(extracted_data).strip()
                else:
                    ad_data[field] = extracted_data.strip() if extracted_data else None
                
            ad_data['url'] = urljoin(response.url, ad_data['url'])
            ad_data['host'] = website
            ad_data['adType'] = adType  # added
            ad_data['objectType'] = objectType  # added
            
            yield ad_data

        self.update_progress(response, len(ads))

    def get_types_from_url(self, url):
        if 'prodaja' in url:
            adType = 'prodaja'
        elif 'izdavanje' in url:
            adType = 'izdavanje'
        else:
            adType = 'unknown'
    
        if 'stanova' in url or 'stanovi' in url or 'stan' in url:
            objectType = 'stan'
        elif 'kuca' in url or 'kuce' in url:
            objectType = 'kuca'
        else:
            objectType = 'unknown'

        return adType, objectType

    def parse_price(self, value):
        if value is None:
            return 'Dogovor'
        
        stripped_value = re.sub(r'\D', '', value)
        return int(stripped_value) if stripped_value else 0

    def parse_surface(self, value):
        if value is None:
            return 0

        # Remove all non-digit characters, except for the dot (.) and comma (,)
        stripped_value = re.sub(r'[^\d.,]', '', value)

        try:
            return float(stripped_value.replace(',', '.'))  # Replace comma with dot for proper float parsing
        except ValueError:
            return 0

    def parse_string(self, value):
        if value is None:
            return ''
        
        translations = {
            "č": "c", "ć": "c", "ž": "z", "š": "s", "đ": "dj",
            "Č": "C", "Ć": "C", "Ž": "Z", "Š": "S", "Đ": "Dj"
        }
        return ''.join(translations.get(c, c) for c in value)

    def parse_date(self, date_string):
        if date_string is None:
            return ''
        
        known_formats = [
            "%d.%m.%Y.",  # Format like: 05.10.2023.
            "%b %d, %Y",  # Format like: Jul 25, 2023
            "%d/%m/%y"    # Format like: 06/10/23
        ]
        date_object = None

        # Special handling for "Postavljen" format
        if "Postavljen" in date_string:
            date_string = re.search(r"Postavljen\s+(.+)\s+na", date_string).group(1)
                
        for date_format in known_formats:
            try:
                date_object = datetime.strptime(date_string, date_format)
                break
            except ValueError:
                pass

        # Convert to uniform format: YYYY-MM-DD
        return date_object.strftime("%Y-%m-%d.") if date_object else date_string
    
    

    def update_progress(self, response, items_scraped_on_current_page):
        self.processed_requests += 1
        if items_scraped_on_current_page == 0:
            self.logger.info(f"Page {response.url} has 0 items.")
        
        self.total_items += items_scraped_on_current_page
        progress_percentage = (self.processed_requests / self.total_requests) * 100
        self.logger.info(f"Page: {self.processed_requests}/{self.total_requests} - Items scraped on this page: {items_scraped_on_current_page} - Total Items: {self.total_items} ------ Complete: {progress_percentage:.2f}% / 100%")

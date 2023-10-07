import scrapy
from ad_scraper.website_configs import WEBSITE_CONFIGS
from urllib.parse import urljoin

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
                for page in range(0, start_url_config['max_pages']):
                    offset = (page - 1) * 20
                    url = f"{base_url}{pagination_pattern.format(page_number=page, offset=offset)}"
                    yield scrapy.Request(url, callback=self.parse, meta={'config': config, 'website': website})

    def parse(self, response):
        config = response.meta.get('config')
        website = response.meta.get('website')
        ads = response.xpath(config['ad_selector'])
        for ad in ads:
            ad_data = {}
            for field, selector in config['fields'].items():
                extracted_data = ad.xpath(selector).get()
                ad_data[field] = extracted_data.strip() if extracted_data else None
            ad_data['url'] = urljoin(response.url, ad_data['url'])
            ad_data['host'] = website
            yield ad_data
        self.processed_requests += 1
        items_scraped_on_current_page = len(ads)

        if items_scraped_on_current_page == 0:
            self.logger.info(f"Page {response.url} has 0 items.")
        
        self.total_items += items_scraped_on_current_page
        progress_percentage = (self.processed_requests / self.total_requests) * 100
        self.logger.info(f"Page: {self.processed_requests}/{self.total_requests} - Items scraped on this page: {items_scraped_on_current_page} - Total Items: {self.total_items} ------ Complete: {progress_percentage:.2f}% / 100%")

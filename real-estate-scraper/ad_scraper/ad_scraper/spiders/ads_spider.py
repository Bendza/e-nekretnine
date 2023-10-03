import scrapy
from ad_scraper.website_configs import WEBSITE_CONFIGS

class AdsSpider(scrapy.Spider):
    name = 'ads_spider'
    total_requests = sum(start_url_config['max_pages'] for config in WEBSITE_CONFIGS.values() for start_url_config in config['start_urls'])
    processed_requests = 0
    total_items = 0 

    def start_requests(self):
        for website, config in WEBSITE_CONFIGS.items():
            self.current_website = website  # Set the current website being processed
            for start_url_config in config['start_urls']:
                base_url = start_url_config['url']
                pagination_pattern = config.get('pagination_pattern', '?page={page_number}')  # Default to '?page={page_number}' if not provided
                for page in range(0, start_url_config['max_pages']):
                    offset = (page - 1) * 20
                    url = f"{base_url}{pagination_pattern.format(page_number=page, offset=offset)}"
                    yield scrapy.Request(url, callback=self.parse, meta={'config': config})

    def parse(self, response):
        config = response.meta['config']
        ad_links = response.css(config['ad_selector'] + '::attr(href)').extract()

        for link in ad_links:
            yield {
                'url': response.urljoin(link)  # This ensures the URL is absolute, not relative
            }

        self.processed_requests += 1
        self.total_items += len(ad_links)

        # Update progress
        progress_percentage = (self.processed_requests / self.total_requests) * 100
        self.logger.info(f" Page: {self.processed_requests}/{self.total_requests} - Items:{self.total_items} ------------------------------------------- Complete: {progress_percentage:.2f}% /100%")

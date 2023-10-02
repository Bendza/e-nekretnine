import scrapy
from ad_scraper.website_configs import WEBSITE_CONFIGS

class AdsSpider(scrapy.Spider):
    name = 'ads_spider'
    total_urls = sum(len(config['start_urls']) for config in WEBSITE_CONFIGS.values())
    processed_urls = 0

    def start_requests(self):
        for config in WEBSITE_CONFIGS.values():
            for start_url_config in config['start_urls']:
                url = start_url_config['url']
                yield scrapy.Request(url, callback=self.parse, meta={'config': config, 'start_url_config': start_url_config})

    def parse(self, response):
        # ... (existing logic)

        # Update progress
        self.processed_urls += 1
        progress_percentage = (self.processed_urls / self.total_urls) * 100
        self.logger.info(f"Progress: {progress_percentage:.2f}%")

    # ... rest of the spider

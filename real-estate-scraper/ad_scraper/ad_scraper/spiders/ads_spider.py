import scrapy
from ad_scraper.website_configs import WEBSITE_CONFIGS

class AdsSpider(scrapy.Spider):
    name = 'ads_spider'
    total_pages = sum(start_url_config['max_pages'] for config in WEBSITE_CONFIGS.values() for start_url_config in config['start_urls'])
    processed_pages = 0

    def start_requests(self):
        for config in WEBSITE_CONFIGS.values():
            for start_url_config in config['start_urls']:
                base_url = start_url_config['url']
                pagination_pattern = config.get('pagination_pattern', '?page={page_number}')  # Default to '?page={page_number}' if not provided
                for page in range(1, start_url_config['max_pages'] + 1):
                    # Construct the URL with the pagination pattern
                    url = f"{base_url}{pagination_pattern.format(page_number=page)}"
                    yield scrapy.Request(url, callback=self.parse, meta={'config': config})

    def parse(self, response):
        config = response.meta['config']
        ad_links = response.css(config['ad_selector'] + '::attr(href)').extract()

        for link in ad_links:
            yield {
                'url': response.urljoin(link)  # This ensures the URL is absolute, not relative
            }

        # Update progress
        self.processed_pages += 1
        progress_percentage = (self.processed_pages / self.total_pages) * 100
        website_domain = response.url.split('/')[2]  # Extracts the domain from the URL
        self.logger.info(f"Progress for {website_domain}: {progress_percentage:.2f}%")

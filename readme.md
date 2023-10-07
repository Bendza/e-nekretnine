Real Estate Scraper with Scrapy and MongoDB
Overview
This project is a web scraping tool built with Scrapy to extract real estate listings from various websites. The scraped data is then stored in a MongoDB database for further analysis or integration into other applications.

Features
Supports multiple real estate websites with customizable configurations.
Handles pagination to scrape data from multiple pages.
Extracts key data fields such as URL, title, price, location, surface area, date, and image URL.
Provides flexibility for adding new websites and adjusting scraping settings.
Getting Started
Follow these steps to get started with the project:

Clone this repository to your local machine.

bash
Copy code
git clone "https://github.com/Bendza/e-nekretnine"
Install the required dependencies.

Copy code
pip install scrapy pymongo
Configure the project settings in settings.py, including MongoDB connection details and other customization options.

Define website configurations in website_configs.py for the websites you want to scrape.

Run the scraper using the following command:

Copy code
scrapy crawl ads_spider
Scraped data will be stored in your MongoDB database, ready for further use.

Customization
Add new websites and their configurations to website_configs.py.
Adjust field selectors and XPath expressions in the website configurations to match the structure of the target websites.
Fine-tune settings in settings.py for your specific scraping needs.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

License
This project is licensed under the MIT License.

Acknowledgments
This project is based on Scrapy, a powerful web scraping framework.
MongoDB is used for data storage.
Happy scraping!
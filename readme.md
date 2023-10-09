e-Nekretnine: Real Estate Scraper & Visualizer
A comprehensive tool to extract real estate listings from various websites, store them in MongoDB, and visualize them using an Electron-based user interface.

Table of Contents
Features
Prerequisites
Getting Started
Customization
Contributing
License
Acknowledgments
Features
Web Scraping: Built on Scrapy, the scraper extracts real estate listings from multiple websites with ease.
Data Storage: All scraped data is systematically stored in MongoDB.
Electron UI: A user-friendly interface to visualize, filter, and analyze the scraped data.
Configurability: Easy customization options to add new websites or adjust scraping settings.
Robustness: Error handling, logging, and retry mechanisms ensure smooth data extraction.
Prerequisites
Python 3.x
MongoDB
Node.js and npm
Getting Started
Setting Up the Scraper
Clone the Repository

bash
Copy code
git clone "https://github.com/Bendza/e-nekretnine"
Navigate to the Project Directory

bash
Copy code
cd e-nekretnine
Activate the Python Environment

bash
Copy code
pip install scrapy pymongo
Adjust Configuration

Update settings.py for MongoDB connection details and scraping configurations.
Modify website_configs.py for target websites and their specific configurations.
Run the Scraper

bash
Copy code
scrapy crawl ads_spider


Setting Up the Electron UI
Install the Required npm Packages

bash
Copy code
npm install
Run the Electron Application

bash
Copy code
npm start
Customization
Websites: Extend scraping capabilities by adding new websites to website_configs.py.
Selectors: Tailor XPath/Selector expressions in the website configurations to adapt to changing website structures.
UI Components: Customize the Electron-based interface to suit your visualization and interaction needs.
Contributing
We welcome contributions to e-Nekretnine! Please open an issue to discuss your ideas or submit a pull request with enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
Thanks to Scrapy for providing the web scraping framework.
MongoDB serves as our dependable database solution.
Electron powers the user interface, ensuring a smooth and intuitive experience.
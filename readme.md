# e-Nekretnine: Real Estate Scraper & Visualizer

A comprehensive tool to extract real estate listings from various websites, store them in MongoDB, and visualize them using an Electron-based user interface.

## 📖 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🌟 Features

- **Web Scraping**: Built on Scrapy, the scraper extracts real estate listings from multiple websites with ease.
- **Data Storage**: All scraped data is systematically stored in MongoDB.
- **Electron UI**: A user-friendly interface to visualize, filter, and analyze the scraped data.
- **Configurability**: Easy customization options to add new websites or adjust scraping settings.
- **Robustness**: Error handling, logging, and retry mechanisms ensure smooth data extraction.

## 🛠 Prerequisites

- Python 3.x
- MongoDB
- Node.js and npm

## 🚀 Getting Started

### Setting Up the Scraper

1. **Clone the Repository**
    ```bash
    git clone "https://github.com/Bendza/e-nekretnine"
    ```

2. **Navigate to the Project Directory**
    ```bash
    cd e-nekretnine
    ```

3. **Install Required Python Dependencies**
    ```bash
    pip install scrapy pymongo
    ```

4. **Adjust Configuration**
    - Update `settings.py` for MongoDB connection details and scraping configurations.
    - Modify `website_configs.py` for target websites and their specific configurations.

5. **Run the Scraper**
    ```bash
    scrapy crawl ads_spider
    ```

### Setting Up the Electron UI

1. **Install the Required npm Packages**
    ```bash
    npm install
    ```

2. **Run the Electron Application**
    ```bash
    npm start
    ```

## 🔧 Customization

- **Websites**: Extend scraping capabilities by adding new websites to `website_configs.py`.
- **Selectors**: Tailor XPath/Selector expressions in the website configurations to adapt to changing website structures.
- **UI Components**: Customize the Electron-based interface to suit your visualization and interaction needs.

## 👥 Contributing

We welcome contributions to `e-Nekretnine`! Please open an issue to discuss your ideas or submit a pull request with enhancements.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 🙌 Acknowledgments

- Thanks to [Scrapy](https://scrapy.org/) for providing the web scraping framework.
- [MongoDB](https://www.mongodb.com/) serves as our dependable database solution.
- [Electron](https://www.electronjs.org/) powers the user interface, ensuring a smooth and intuitive experience.


# Ecommerce Web Scraper

## Overview

This Python-based web scraper is designed to extract product information from ecommerce websites using the Beautiful Soup library. It provides a flexible and customizable solution for gathering data from various online stores.

## Features

- **Easy-to-Use:** Simple Python script for scraping product information.
- **Beautiful Soup Integration:** Leverages the power of Beautiful Soup for HTML parsing.
- **Customizable:** Easily adapt the script to different ecommerce websites and product structures.

## Getting Started

### Prerequisites

- Python installed on your machine.
- Flask (install using `pip install Flask`)
- pandas (install using `pip install pandas`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/anushravrathi/Ecommerce-Web-Scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Ecommerce-Web-Scraper
    ```

## Usage

1. Run the web scraper (`scraper.py`) to collect data from the target website:

    ```bash
    python scraper.py
    ```

   This will generate a CSV file (`data/data.csv`) containing the extracted information.

2. Run the Flask web application (`app.py`) to display the results:

    ```bash
    python app.py
    ```

   Access the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

   The Flask application uses HTML templates for rendering. The main template file (`index.html`) is located in the `templates` folder.

## Project Structure

- `scraper.py`: Python script for web scraping.
- `app.py`: Flask web application script.
- `data/`: Folder containing the CSV file with extracted data.
- `templates/`: Folder containing HTML templates for the web application.

## Customization

The script is designed to be adaptable to different ecommerce websites. Customize the HTML element selectors and parsing logic in the `webScraping ecomm.py` file according to the structure of the target website.

## Notes

- Ensure that you have an active internet connection while running the web scraper to fetch data from the specified website.
- The Flask web application will display the results in a tabular format on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Contributing

We welcome contributions! If you encounter issues or want to enhance the scraper for additional features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or improvement.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## Contact

- **Anushrav Rathi**
- Email: ranushrav@gmail.com
- LinkedIn: [Anushrav Rathi's LinkedIn Profile](https://www.linkedin.com/in/anushravrathi/)
- GitHub: [anushravrathi](https://github.com/anushravrathi)

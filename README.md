# Web Scraper Application

A Flask-based web application for scraping website content and extracting links.

## Features

- Scrape multiple websites simultaneously
- Extract page titles and main content
- Display found links from each page
- Simple web interface for easy use

## Installation

1. open terminal and navigate to the project directory:

   ```bash
   cd search-engine
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your browser to:

   ```
   http://localhost:5000
   ```

3. Enter website URLs (one per line) in the text area and click "Scrape"

## Example Input

```
https://www.example.com
https://en.wikipedia.org/wiki/Web_scraping
https://www.python.org
```

## Project Structure

```
search-engine/
├── app.py                # Main application file
├── requirements.txt      # Dependencies
├── templates/            # HTML templates
│   └── index.html        # Main interface
└── README.md             # This file
```

## Limitations

- May not work with JavaScript-heavy websites
- Some websites may block scraping attempts
- Limited to scraping publicly accessible pages

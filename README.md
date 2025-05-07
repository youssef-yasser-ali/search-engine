# Search Engine Application

A Flask-based web application for scraping website content and extracting links.

## Features

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

## Configuration

1. download these inverted index file from Google Drive and place them in the project directory:

   ```bash
   gdown https://drive.google.com/uc?id=1KBHb6r_i3KbQkXvnaITCWQkCIv4TLm_5

   ```

2. extract the inverted index files:

   ```bash
   bzip2 -d output.txt.bz2
   ```

3. Make sure you have the following files in the project directory:

   ```
   output.txt
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

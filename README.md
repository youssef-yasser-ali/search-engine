# Search Engine Application

A Flask-based web application for searching through scraped website content with a clean web interface.

## Features

- **Web Search Interface**: Clean HTML/CSS frontend
- **API Endpoint**: `/api/search` for programmatic access
- **Template Inheritance**: Efficient HTML structure using `base.html`
- **Pagination**: Built-in support for large result sets

## Installation

1.  navigate to the project directory:

```bash
cd search-engine
```

2. Create and activate a virtual environment:

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Download and prepare the inverted index file:

```bash
gdown https://drive.google.com/uc?id=1KBHb6r_i3KbQkXvnaITCWQkCIv4TLm_5
bzip2 -d output.txt.bz2
```

## Usage

### Running the Application

```bash
python app.py
```

Access the application at: `http://localhost:5000`

### API Usage

Make GET requests to:

```
http://localhost:5000/api/search?q=your_query
```

Example response:

```json
{
  "query": "your_query",
  "results": [...],
  "count": 25
}
```

## Project Structure

```
search-engine/
├── app.py                # Main application (Flask routes)
├── utils.py              # Search functionality
├── static/
│   └── css/
│       └── style.css     # Custom styles
├── templates/
│   ├── base.html         # Base template with common structure
│   ├── index.html        # Homepage template
│   └── search.html       # Search results page template
├── data/                 # Folder containing part_*.txt files with URLs
│   ├── part_1.txt
│   ├── part_2.txt
│   ├── part_3.txt
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Development

- **Debug Mode**: Automatically enabled when running `app.py`
- **Auto-Reload**: Templates and static files update without restart
- **Debugger PIN**: Shown in console for error debugging

## Limitations

- Requires pre-built inverted index (output.txt)
- Currently uses basic string matching in search
- No authentication or rate limiting on API

## Future Improvements

- Add proper search ranking
- Implement incremental indexing
- Add user accounts and search history

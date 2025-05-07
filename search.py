from flask import Flask, request, render_template, jsonify
from utils import decode_url, search_word

app = Flask(__name__)

@app.route('/')
def index():
    """Render the search UI"""
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def api_search():
    """API endpoint for searching URLs"""
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Missing search query"}), 400
    
    results = search_word(query)
    return jsonify({
        "query": query,
        "results": results,
        "count": len(results)
    })

@app.route('/search', methods=['GET'])
def web_search():
    """Web interface for searching URLs"""
    query = request.args.get('q', '')
    results = []
    
    if query:
        results = search_word(query)
    
    return render_template('search.html', query=query, results=results)

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    import os
    os.makedirs('templates', exist_ok=True)
    
    # Create default templates if they don't exist
    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w') as f:
            f.write('''<!DOCTYPE html>
<html>
<head>
    <title>URL Search</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .search-box { margin: 20px 0; }
        input[type="text"] { padding: 8px; width: 300px; }
        button { padding: 8px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { margin: 10px 0; padding: 10px; border: 1px solid #ddd; }
        .result a { color: #007bff; text-decoration: none; }
        .result a:hover { text-decoration: underline; }
        .api-info { margin-top: 30px; padding: 15px; background: #f5f5f5; }
    </style>
</head>
<body>
    <h1>URL Search</h1>
    <div class="search-box">
        <form action="/search" method="get">
            <input type="text" name="q" placeholder="Enter search term..." required>
            <button type="submit">Search</button>
        </form>
    </div>
    
    <div class="api-info">
        <h2>API Usage</h2>
        <p>You can also use our search API:</p>
        <code>GET /api/search?q=your_search_term</code>
        <p>Example: <a href="/api/search?q=youssef" target="_blank">/api/search?q=youssef</a></p>
    </div>
</body>
</html>''')

    if not os.path.exists('templates/search.html'):
        with open('templates/search.html', 'w') as f:
            f.write('''<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .search-box { margin: 20px 0; }
        input[type="text"] { padding: 8px; width: 300px; }
        button { padding: 8px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background: #0056b3; }
        .result { margin: 10px 0; padding: 10px; border: 1px solid #ddd; }
        .result a { color: #007bff; text-decoration: none; }
        .result a:hover { text-decoration: underline; }
        .back-link { display: block; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Search Results for "{{ query }}"</h1>
    
    <div class="search-box">
        <form action="/search" method="get">
            <input type="text" name="q" placeholder="Enter search term..." value="{{ query }}" required>
            <button type="submit">Search</button>
        </form>
    </div>
    
    {% if results %}
        <p>Found {{ results|length }} results:</p>
        {% for url in results %}
            <div class="result">
                <a href="{{ url }}" target="_blank">{{ url }}</a>
            </div>
        {% endfor %}
    {% else %}
        {% if query %}
            <p>No results found for "{{ query }}"</p>
        {% endif %}
    {% endif %}
    
    <a href="/" class="back-link">← Back to search</a>
</body>
</html>''')

    app.run(debug=True)
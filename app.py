from flask import Flask, request, render_template, jsonify

from utils import search_word


app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/search')
# def api_search():
#     if not (query := request.args.get('q', '').strip()):
#         return jsonify({"error": "Missing query"}), 400
#     return jsonify({
#         "query": query,
#         "results": search_word(query),
#         "count": len(search_word(query))
#     })

@app.route('/search')
def web_search():
    query = request.args.get('q', '').strip()
    results = search_word(query) if query else []
    return render_template('search.html', query=query, results=results)


if __name__ == '__main__':
    app.run(debug=True)

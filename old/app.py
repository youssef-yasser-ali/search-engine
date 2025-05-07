from flask import Flask, render_template, request, flash
from old.helper_functions import scrape_page, build_index
from collections import defaultdict

app = Flask(__name__)



# Simple storage (replace with database in production)
pages = {}
index = defaultdict(list)



@app.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        if 'urls' in request.form:
            urls = [url.strip() for url in request.form['urls'].split('\n') if url.strip()]
            
            for url in urls:
                page = scrape_page(url)
                if page:
                    pages[url] = page
                    build_index(page , index)
            
            flash(f"Scraped {len(urls)} pages", 'success')
        
        elif 'query' in request.form:
            query = request.form['query'].lower()

            if not query:
                flash("Please enter a search query", 'error')
                return render_template('index.html', results=None)



            results = []
            
            for word in query.split():
                if word in index:
                    results.extend(index[word])
            
            # Remove duplicates and get page details
            unique_results = []
            seen = set()
            for url in results:
                if url not in seen and url in pages:
                    seen.add(url)
                    unique_results.append(pages[url])
            
            return render_template('index.html', results=unique_results, query=query)
    
    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
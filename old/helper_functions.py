import requests
from bs4 import BeautifulSoup





def scrape_page(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        

        
        text = soup.get_text(separator=' ', strip=True)
        title = soup.title.string if soup.title else url
        
        return {
            'url': url,
            'title': title,
            'content': text
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def build_index(page , index):
    words = page['content'].lower().split()
    for word in set(words):  
        if len(word) > 3:    
            index[word].append(page['url'])
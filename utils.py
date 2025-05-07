import os
from urllib.parse import unquote

def decode_url(encoded_text):
    try:
        # Remove metadata (like (1)) if present
        if "(" in encoded_text and encoded_text.endswith(")"):
            encoded_text = encoded_text.split("(")[0]

        print('url after encoding : ', encoded_text)

        encoded_text = encoded_text.replace('_', '/')

        # Decode the URL
        url_path = unquote(encoded_text)
        
        # Ensure it starts with https://
        if not url_path.startswith("http"):
            url_path = f"https://{url_path}"
            
        return url_path
    except Exception as e:
        print(f"Warning: Could not decode URL '{encoded_text}': {str(e)}")
        return encoded_text

def search_word(word, file_path="output.txt"):
    """Search for word in index file and return properly formatted App Store URLs"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            next(f)  # Skip header
            for line in f:
                if line.startswith(word + "|"):
                    parts = line.strip().split("|")
                    if len(parts) >= 3:
                        urls = parts[2].split(" ")
                        return [decode_url(u) for u in urls]
        return []
    except FileNotFoundError:
        return []
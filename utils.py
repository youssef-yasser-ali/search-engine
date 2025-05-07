import os
from urllib.parse import unquote

def decode_url(encoded_text):
    try:
        if "(" in encoded_text and encoded_text.endswith(")"):
            encoded_text = encoded_text.rsplit("(", 1)[0]

        return unquote(encoded_text)


        
    except Exception as e:
        print(f"Warning: Could not decode URL '{encoded_text}': {str(e)}")
        return encoded_text

def search_word(word, folder="data"):
    """Search all part_*.txt files in the specified folder for a word and return decoded URLs"""
    decoded_urls = []
    try:
        for file in sorted(f for f in os.listdir(folder) if f.startswith("part_") and f.endswith(".txt")):
            file_path = os.path.join(folder, file)  # Build the full file path
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.read().strip().split("\n")
                for line in lines[1:]:  # Skip the first line (if necessary)
                    parts = line.strip().split("|||")
                    if len(parts) >= 3 and parts[0].strip() == word:
                        urls = parts[2].strip().split(" ")
                        decoded_urls.extend(decode_url(u) for u in urls if u)
    except Exception as e:
        print(f"Failed to read files in folder '{folder}': {e}")
    return decoded_urls

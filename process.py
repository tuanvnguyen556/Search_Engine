import json
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import nltk 
def file_processor(given_file):
    """
    This function processes the json file and retrieves the html content.
    Then, the html content is processed.
    """
    nltk.download('punkt')
    tokens = []
    
    open_file = open(given_file, errors='ignore') #opens the file
    try:
        data = json.load(open_file) #loads the json format
        
        soup = BeautifulSoup(data['content'], 'html.parser') #parses html
        text = soup.get_text(strip=True) #retrieves the content
        textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text) #does some stripping of characters
        tokens = word_tokenize(textWithoutSymbols.lower()) #tokenizes the string and lowercases them
    except Exception as e:
        pass
    return tokens
    open_file.close()


if __name__ == "__main__":
    pass
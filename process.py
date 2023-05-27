import json
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from fragment import Remove_fragments
from postings import docID_counter # Creates a Posting object
import requests

import nltk 
def file_processor(given_file):
    """
    This function processes the json file and retrieves the html content.
    Then, the html content is processed.
    """
    tokens = []
    data = None
    open_file = open(given_file, errors='ignore') #opens the file
    docID_counter.increment() # increment the ID by 1
    try:
        data = json.load(open_file) #loads the json format
        create_request = requests.get(data['url'])
        if 200 <= create_request.status_code < 400:
            fragmenter = Remove_fragments()
            if not fragmenter.remove_fragment(data['url']):
                return tokens, data
            soup = BeautifulSoup(create_request.text, 'html.parser') #parses html
            text = soup.get_text(strip=True) #retrieves the content
            textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text) #does some stripping of characters
            tokens = word_tokenize(textWithoutSymbols.lower()) #tokenizes the string and lowercases them
    except Exception as e:
        pass #ignore the error
    open_file.close()

    return tokens, data
    


if __name__ == "__main__":
    pass
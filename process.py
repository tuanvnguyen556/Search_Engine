import json
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from fragment import Remove_fragments
import requests

import nltk 
def file_processor(given_file):
    """
    This function processes the json file and retrieves the html content.
    Then, the html content is processed.
    """
    tokens = []
    data = None #initial state to determine if a file can be processed

    open_file = open(given_file, errors='ignore') #opens the file
    try:
        data = json.load(open_file) #loads the json format
        create_request = requests.get(data['url'])
        if 200 <= create_request.status_code < 400: #makes sure status code is within range
            fragmenter = Remove_fragments()
            fragment_url = fragmenter.remove_fragment(data['url'])
            if data and 'url' in data:
                data['url'] = fragment_url #changes the url to become the fragment_url
            if not fragment_url:
                return tokens, data #returns data == None and token == []
            
            soup = BeautifulSoup(create_request.text, 'html.parser') #parses html
            text = soup.get_text(strip=True) #retrieves the content
            textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text) #does some stripping of characters
            tokens = word_tokenize(textWithoutSymbols.lower()) #tokenizes the string and lowercases them
    except Exception as e:
        pass #ignore the error
    open_file.close()
    print(data["url"])
    return tokens, data #data is used for truthy boolean comparison to see if a json object was returned
    #data == None, then can't process the file
    #data == json object, then file was processed 
    


if __name__ == "__main__":
    pass
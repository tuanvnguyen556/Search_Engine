import json
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

from posting_dictionary import Posting_Dict # these are for creating a posting and adding it to 
from postings import Posting, docID_counter # Creates a Posting object

import nltk 
def file_processor(given_file):
    """
    This function processes the json file and retrieves the html content.
    Then, the html content is processed.
    """
    tokens = []
    
    open_file = open(given_file, errors='ignore') #opens the file
    docID_counter.increment() # increment the ID by 1
    try:
        data = json.load(open_file) #loads the json format
        
        soup = BeautifulSoup(data['content'], 'html.parser') #parses html
        text = soup.get_text(strip=True) #retrieves the content
        textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text) #does some stripping of characters
        tokens = word_tokenize(textWithoutSymbols)
        Posting_Dict.addPosting(docID=InvertedIndex.docID, posting=Posting(url=data['url'], encoding=data['encoding'], content=text))
        tokens = word_tokenize(textWithoutSymbols.lower()) #tokenizes the string and lowercases them
    except Exception as e:
        print(e)
    open_file.close()
    return tokens


if __name__ == "__main__":
    pass
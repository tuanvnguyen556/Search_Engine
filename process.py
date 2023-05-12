import json
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

from inverted_index import InvertedIndex # these are for creating a posting and adding it to 
from postings import Posting, docID_counter # Creates a Posting object


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
        InvertedIndex.addPosting(docID=docID_counter.docID, posting=Posting(url=data['url'], encoding=data['encoding'], content=text))
    except Exception as e:
        print(e) # skip any errors, but notify the user as well
    open_file.close()
    return tokens


if __name__ == "__main__":
    given_file = r"developer/DEV/aiclub_ics_uci_edu/8ef6d99d9f9264fc84514cdd2e680d35843785310331e1db4bbd06dd2b8eda9b.json"
    file_processor(given_file)
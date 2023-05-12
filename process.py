import json
import re
from bs4 import BeautifulSoup

def file_processor(given_file):
    """
    This function processes the json file and retrieves the html content.
    Then, the html content is processed.
    """
    open_file = open(given_file, errors='ignore') #opens the file
    try:
        data = json.load(open_file) #loads the json format
        
        soup = BeautifulSoup(data['content'], 'html.parser') #parses html
        text = soup.get_text(strip=True) #retrieves the content
        textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text) #does some stripping of characters

        return textWithoutSymbols
    except:
        pass
    open_file.close()


if __name__ == "__main__":
    pass
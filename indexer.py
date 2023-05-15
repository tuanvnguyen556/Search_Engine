from bs4 import BeautifulSoup
from read_files import read_files
import nltk

def index():
    nltk.download('punkt')
    file = "developer/DEV/aiclub_ics_uci_edu"
    read_files(file)
    # for each term... 
        # InvertedIndex.addToInverted(term, list[tuples of id, position]) # adds each term/position tuple to inverted index


if __name__ == "__main__":
    index()
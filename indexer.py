from bs4 import BeautifulSoup
from inverted_index import InvertedIndex
import nltk
def index():
    nltk.download('punkt')
    # for each term... 
        # InvertedIndex.addToInverted(term, list[tuples of id, position]) # adds each term/position tuple to inverted index
    # InvertedIndex.addPosting(document ID, posting) # per document ID, adds the resulting posting


if __name__ == "__main__":
    pass

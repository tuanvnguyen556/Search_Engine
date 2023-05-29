from indexer import index,jsonfied, jsonfied_posting, tsvfied
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
import json


if __name__ == "__main__":
    index()
    jsonfied(InvertedIndex.InvertedIndexDict)
    jsonfied_posting(Posting_Dict.ID_Posting)
    with open("indexer.txt") as f1:
        InvertedIndex.InvertedIndexDict = json.load(f1)
    
    tsvfied(InvertedIndex.InvertedIndexDict)
    InvertedIndex.write_to_file()


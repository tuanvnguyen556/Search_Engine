from indexer import index,jsonfied, jsonfied_posting, tsvfied
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
import json

def running_indexer():
    index()
    jsonfied(InvertedIndex.InvertedIndexDict)
    jsonfied_posting(Posting_Dict.ID_Posting)


if __name__ == "__main__":
    running_indexer()
   


from indexer import index,jsonfied, jsonfied_posting
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
import json


if __name__ == "__main__":
    index()
    #jsonfied(InvertedIndex.InvertedIndexDict)
    jsonfied_posting(Posting_Dict.ID_Posting)
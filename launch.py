from indexer import index,jsonfied
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
import json


if __name__ == "__main__":
    index()
    convertToJson = jsonfied(InvertedIndex.InvertedIndexDict, Posting_Dict.ID_Posting)

from indexer import index,jsonfied
from inverted_index import InvertedIndex
import json


if __name__ == "__main__":
    index()
    convertToJson = jsonfied(InvertedIndex.InvertedIndexDict)

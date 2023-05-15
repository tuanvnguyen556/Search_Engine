from indexer import index,jsonfied
from inverted_index import InvertedIndexDict
import json


if __name__ == "__main__":
    index()
    convertToJson = jsonfied(InvertedIndexDict)

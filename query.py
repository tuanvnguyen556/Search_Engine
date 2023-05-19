""" Run this file and enter a query from the terminal. """

import sys
import json
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
def main() -> None:
    with open("indexer.txt") as f1:
        InvertedIndex.InvertedIndexDict = json.load(f1)
    
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)
        
    while True:
        query = input("Enter a query: ").lower()
        if not query:
            print("Please enter a query.")
        elif query == "quit the query":
            break
        else:
            retrieve_doc = booleanRetrieval()
            top_urls = retrieve_doc.booleanAndRetrieval(query)
            

    
        


    # lst_doc_IDs = some_intersection_function(*[inverted_index.InvertedIndex[term] for term in query])
    # printer(doc_IDs)
    

    

if __name__ == "__main__":
    main()
""" Run this file and enter a query from the terminal. """

import sys
import inverted_index
import json
from booleanRetrieval import booleanRetrieval
def main() -> None:
    with open("indexer.txt") as f1:
        inverted_index = json.load(f1)
    
    with open("posting.txt") as f2:
        the_posting = json.load(f2)
        
    while True:
        query = input("Enter a query: ").lower()
        if not query:
            print("Please enter a query.")
        elif query == "quit the query":
            break
        else:
            retrieve_doc = booleanRetrieval()
            print(retrieve_doc.booleanAndRetrieval(query))
            

    
        


    # lst_doc_IDs = some_intersection_function(*[inverted_index.InvertedIndex[term] for term in query])
    # printer(doc_IDs)
    

    

if __name__ == "__main__":
    main()
""" Run this file and enter a query from the terminal. """

import sys
import inverted_index
import json

def main() -> None:
    with open("indexer.txt") as f:
        inverted_index = json.load(f)
    while True:
        query = input("Enter a query:")
        if not query:
            print("Please enter a query.")
            continue
        query = query.lower() # lowercase query
        

    # lst_doc_IDs = some_intersection_function(*[inverted_index.InvertedIndex[term] for term in query])
    # printer(doc_IDs)
    

    

if __name__ == "__main__":
    main()
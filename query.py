""" Run this file and enter a query from the terminal. """
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
            retrieve_doc = booleanRetrieval(query)
            save_docIDs = retrieve_doc.booleanAndRetrieval()
            retrieve_doc.print_urls(save_docIDs)

            



if __name__ == "__main__":
    main()
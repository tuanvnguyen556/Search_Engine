""" Run this file and enter a query from the terminal. """
import json
import csv
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList

def main() -> None:
    with open("indexer_positions.json") as f1:
        positions_dict = json.load(f1)
    
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)
    
    with open("indexer.tsv", "r") as f:    
        file = csv.reader(f, delimiter='\t')
        while True:
            query = input("Enter a query: ").lower()
            if not query:
                print("Please enter a query.")
            elif query == "quit the query":
                break
            else:
                queryList = query.split()
                lstPos = []
                for q in queryList:
                    if q in positions_dict:
                        lstPos.append(getTSVList(f, q, positions_dict[q]))
                
                if not lstPos: # no query terms exist in the corpus
                    continue
                else:
                    print(lstPos)
                    #retrieve_doc = booleanRetrieval(query)
                    #save_docIDs = retrieve_doc.booleanAndRetrieval()
                    #retrieve_doc.print_urls(save_docIDs)

            



if __name__ == "__main__":
    main()
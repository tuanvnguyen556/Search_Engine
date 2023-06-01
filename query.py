""" Run this file and enter a query from the terminal. """
import json
import csv
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList
from tf_idf import Calculatetfidf
import time

def main() -> None:
    with open("indexer_positions.json") as f1:
        positions_dict = json.load(f1)
    
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)

    with open("idf_scores.json") as f3:
        Calculatetfidf.idf_map = json.load(f3)
    
    with open("indexer.tsv", "r") as f:    
        file = csv.reader(f, delimiter='\t')
        boolRetrieve = booleanRetrieval()
        while True:
            query = input("Enter a query: ").lower()
            if not query:
                print("Please enter a query.")
            elif query == "quit the query":
                break
            else:
                start = time.time()
                queryList = query.split()
                lstPos = []
                orderedQueryList = sorted([(term, Calculatetfidf.idf_map[term]) for term in queryList], key=lambda x: x[1], reverse=True)
                for i in range(min(5, len(orderedQueryList))):
                    word = orderedQueryList[i]
                    if word in positions_dict:
                        lstPos.append(getTSVList(f, orderedQueryList[i], positions_dict[word]))
                
                if not lstPos: # no query terms exist in the corpus
                    continue
                else:
                    retrieve_doc = boolRetrieve.booleanAndRetrieval(query, *lstPos)
                    end = time.time()
                    print(end - start)
                    #save_docIDs = retrieve_doc.booleanAndRetrieval()
                    #retrieve_doc.print_urls(save_docIDs)

            



if __name__ == "__main__":
    main()
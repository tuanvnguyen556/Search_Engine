""" Run this file and enter a query from the terminal. """
import json
import csv
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList2 as getTSVList
from tf_idf import Calculatetfidf
import time

def main() -> None:
    print("Query loading...")
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
            end1 = time.time()
            query = input("Enter a query: ").lower()
            if not query:
                print("Please enter a query.")
            elif query == "quit the query":
                break
            else:
                start = time.time()
                queryList = query.split()
                lstPos = []
                orderedQueryList = sorted([(term, Calculatetfidf.idf_map[term]) for term in queryList if term in Calculatetfidf.idf_map], key=lambda x: x[1], reverse=True)
                dict_vals = {}
                maxKey = 0 # first maxKey is not used, used for every term afterward
                for i in range(min(5, len(orderedQueryList))):
                    word = orderedQueryList[i][0]
                    if word in positions_dict:
                        dict_vals, maxKey = getTSVList(f, orderedQueryList[i], positions_dict[word], dict_vals, maxKey)
                
                if not dict_vals: # no query terms exist in the corpus
                    print("Query terms do not exist. Please try a different search.")
                    continue
                else:
                    # dict_vals : {1: [[positions], [positions], [positions]]}
                    #retrieve_doc = boolRetrieve.booleanAndRetrieval(query, *lstPos)
                    Calculatetfidf.calculate_tf_idf()
                    end = time.time()
                    print(dict_vals)
                    print((end - start) * 1000, "ms")
                    #print(dict_vals)
                    #save_docIDs = retrieve_doc.booleanAndRetrieval()
                    #retrieve_doc.print_urls(save_docIDs)

        # [[1, 2, 4, 8], [3, 5, 9], [10]]
            



if __name__ == "__main__":
    main()
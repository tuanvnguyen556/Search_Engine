""" Run this file and enter a query from the terminal. """
import json
import csv
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList2 as getTSVList
from tf_idf import Calculatetfidf
import time
from multi_query import kevin_multi_query

def main() -> None:
    stop_words = ['of', 'and', 'the', 'to', 'a', 'in', 'for', 'is', 'on', 'at', 'with', 'this', 'by', 'that', 'or', 'from', 'are', 'be', 'as', 'an']
    print("Query loading...")
    with open("indexer_positions.json") as f1:
        positions_dict = json.load(f1)
    
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)

    with open("idf_scores.json") as f3:
        Calculatetfidf.idf_map = json.load(f3)
    
    with open("indexer.tsv", "r") as f:    
        file = csv.reader(f, delimiter='\t')
        #boolRetrieve = booleanRetrieval()
        while True:
            end1 = time.time()
            query = input("Enter a query: ").lower()
            if not query:
                print("Please enter a query.")
            elif query == "quit the query":
                break
            else:
                start = time.time()
                queryList = list(set(query.split()))

                num_stop = 0 #counts how many stop_words are in query
                for i in queryList:
                    if i in stop_words:
                        num_stop += 1 #adds 1 to stop word counter

                orderedQueryList = sorted([(term, Calculatetfidf.idf_map[term]) for term in queryList if term in Calculatetfidf.idf_map], key=lambda x: x[1], reverse=True)
                
                if num_stop / len(queryList) == 1.0 and len(queryList) >= 2: #threshold for num of stop_words
                    orderedQueryList = orderedQueryList[:num_stop // 2]
                elif num_stop / len(queryList) >= .4 and len(queryList) >= 2:
                    orderedQueryList = orderedQueryList[:-num_stop]

                dict_vals = {}
                maxKey = 0 # first maxKey is not used, used for every term afterward
                for i in range(len(orderedQueryList)):
                    word = orderedQueryList[i][0]
                    if word in positions_dict:
                        dict_vals, maxKey = getTSVList(f, orderedQueryList[i], positions_dict[word], dict_vals, maxKey)
                    else:
                        orderedQueryList.remove(word)
                if not dict_vals: # no query terms exist in the corpus
                    print("Query terms do not exist. Please try a different search.")
                    continue
                else:
                    # if len(queryList) == len(orderedQueryList):
                    #     map_reconstruct = kevin_multi_query(queryList, dict_vals, orderedQueryList)
                    # else:
                    #     map_reconstruct = dict_vals # just so conditional works
                    final_urls = sorted([(docs, tf_idf) for docs, tf_idf in \
                                  Calculatetfidf.calculate_tf_idf(dict_vals,orderedQueryList).items()], key=(lambda x: -x[1]))
                    
                    i = 0
                    count = 0
                    while i < len(final_urls):
                        if Posting_Dict.ID_Posting[str(final_urls[i][0])]['url']:
                            print(Posting_Dict.ID_Posting[str(final_urls[i][0])]['url'])
                            if count % 5 == 4:
                                end = time.time()
                                print((end - start) * 1000, "ms")
                                if input('Enter "more" to see more queries (press any other key otherwise): ') != "more":
                                    break
                            count += 1
                            i += 1
                        else:
                            i += 1
 
            



if __name__ == "__main__":
    main()
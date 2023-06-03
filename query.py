""" Run this file and enter a query from the terminal. """
import json
import csv
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList2 as getTSVList
from tf_idf import Calculatetfidf
import time
from multi_query import kevin_multi_query

def main() -> None:
    # Initialize a list of stop words 
    stop_words = ['of', 'and', 'the', 'to', 'a', 'in', 'for', 'is', 'on', 'at', 'with', 'this', 'by', 'that', 'or', 'from', 'are', 'be', 'as', 'an']
    print("Query loading...")
    # Open indexerPositions json file, load the file content in positions Dict on RAM memory.
    with open("indexer_positions.json") as f1:
        positions_dict = json.load(f1)
        
    # Open posting text file, load the postings content in postingsDict which is also a dictionary structure.
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)
        
    # Open idfScores json file, load the calculated idf into idfMap
    with open("idf_scores.json") as f3:
        Calculatetfidf.idf_map = json.load(f3)
    
    # Open the indexer tsv file as read-only
    with open("indexer.tsv", "r") as f:
        file = csv.reader(f, delimiter='\t')
        #boolRetrieve = booleanRetrieval()
        
        # Run and ask for queries until user indicates to "quit the query".
        while True:
            end1 = time.time()
            query = input("Enter a query: ").lower()
            if not query:
                print("Please enter a query.")
            elif query == "quit the query":
                break
            else:
                
                queryList = list(set(query.split()))
                
                # Keep track of the total number of stop words
                num_stop = 0 #counts how many stop_words are in query
                for i in queryList:
                    if i in stop_words:
                        num_stop += 1 #adds 1 to stop word counter
                # Initialize an orderedQueryList which sorts terms in the queryList by the basis of each token in the query's tf-idf value.
                orderedQueryList = sorted([(term, Calculatetfidf.idf_map[term]) for term in queryList if term in Calculatetfidf.idf_map], key=lambda x: x[1], reverse=True)
                
                # Optimize the orderedQueryList by shortening it by avoiding stop words
                if num_stop / len(queryList) == 1.0 and len(queryList) >= 2: #threshold for num of stop_words
                    orderedQueryList = orderedQueryList[:num_stop // 2]
                elif num_stop / len(queryList) >= .4 and len(queryList) >= 2:
                    orderedQueryList = orderedQueryList[:-num_stop]

                # Initialize a dictionary that will act as the corpus of queries with max Values
                dict_vals = {}
                maxKey = 0 # first maxKey is not used, used for every term afterward
                for i in range(len(orderedQueryList)):
                    word = orderedQueryList[i][0]
                    if word in positions_dict:
                        dict_vals, maxKey = getTSVList(f, orderedQueryList[i], positions_dict[word], dict_vals, maxKey)
                    else:
                        dict_vals = {} # term in query does not exist in any documents
                        break
                    if not dict_vals: # no documents in boolean AND, should break out of loop and return that no docs exist
                        break
                                        
                if not dict_vals: # no query terms exist in the corpus
                    print("This set of terms do not exist together. Please try a different search.")
                    continue
                else:
                    # if len(queryList) == len(orderedQueryList):
                    #     map_reconstruct = kevin_multi_query(queryList, dict_vals, orderedQueryList)
                    # else:
                    #     map_reconstruct = dict_vals # just so conditional works
                    # Amass the final list of urls based of their tf_idf values
                    final_urls = sorted([(docs, tf_idf) for docs, tf_idf in \
                                  Calculatetfidf.calculate_tf_idf(dict_vals,orderedQueryList).items()], key=(lambda x: -x[1]))
                    
                    i = 0
                    count = 0
                    # Iterate over the final_url List until empty
                    while i < len(final_urls):
                        # Check if the key is url in postingDict's posting
                        if Posting_Dict.ID_Posting[str(final_urls[i][0])]['url']:
                            # If so, print the url
                            print(Posting_Dict.ID_Posting[str(final_urls[i][0])]['url'])
                            # Check for first 5 urls
                            if count % 5 == 4:
                                # After processing the first 5 urls, indicate the time taken as well as print it out 
                                
                                if input('Enter "more" to see more queries (press any other key otherwise): ') != "more":
                                    break
                            count += 1
                            i += 1
                        else:
                            i += 1


if __name__ == "__main__":
    main()
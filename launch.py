from indexer import index,jsonfied, jsonfied_posting
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
'''
This script is the first half of the assignment.
This is the script to launch the indexer.
'''

def running_indexer():
    index() #goes through the directory and processes urls of interest
    jsonfied(InvertedIndex.InvertedIndexDict) #throws inverted index into a txt file
    jsonfied_posting(Posting_Dict.ID_Posting) #throws posting into a txt file
    
    InvertedIndex.write_to_file() #if the inverted index dict reaches its size limit, then it will wrote to another file
    InvertedIndex.write_positions() #stores the positions of token and other information



if __name__ == "__main__":
    running_indexer() #launches indexer
   


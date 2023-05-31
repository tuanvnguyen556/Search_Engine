from indexer import index,jsonfied, jsonfied_posting
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict


def running_indexer():
    index()
    jsonfied(InvertedIndex.InvertedIndexDict)
    jsonfied_posting(Posting_Dict.ID_Posting)
    
    InvertedIndex.write_to_file()
    InvertedIndex.write_positions()



if __name__ == "__main__":
    running_indexer()
   


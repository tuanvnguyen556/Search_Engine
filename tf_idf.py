from inverted_index import InvertedIndex
from math import log10
import json

class Calculatetfidf:
    """This function calaculates the term frequency and inverted document frequency for each term
     This function will accept a tsv txt file that contains the inverted index
    content and recieve each token. With every recieved token, this function will
    calculate the tf-idf value for each token given the other information that is next to
    the token in the tsv file. the term frequency will be determined from the tsv file, while 
    the document frequency will be recieved from the InvertedIndexDict.
    
    Formula : W [sub(t,d)] = (1 + log(tf [sub(t, d)])) x log(N / df [sub(t)])
    N = total documents
    tf = number of time that t occurs in d -> tsv file 
    df = number of documents that contain t -> frequency in InvertedIndex
    """
    tf_idf_map = dict() # Stores the tf-idf of each term
    idf_map = dict()

    #of the format: {Token : [doc1: tf-idf, doc2: tf-idf} Token2: {}, ...}

    @classmethod
    def update_tf(cls, filename: str):
        with open("indexer.txt") as indexer:
            InvertedIndex.InvertedIndexDict = json.load(indexer)
    
    @classmethod
    def calculate_tf(cls):
        """ All pseudo code, please change later """
        N = InvertedIndex.docID
        
        for k in InvertedIndex.keys():
            # Structure of Inv. Index: {Token: [frequency, [docID, pos1, pos2, ...], [docID2, pos1, pos2, ...], ...]}
            tf_list = [] # TF listing for the current token
            for t in InvertedIndex[k][1:]:
                tf_list.append(len(t) - 1) # the TF of each term is the (len-1) from removing the first docID

            df = int() # TODO
    
    @classmethod
    def calculate_tf_idf(cls, tf: dict, orderedQueryList: list):
        """This function calculates the tf-idf for every query term"""
        for docs, terms in tf.items(): # docs: docIDs, terms: [[], []]
          
            store_tf_idf = 0
            for i in range(len(terms)): #pos are the lengths of the list
               
                store_tf_idf += (1 + log10(len(terms[i]) - 1)) * cls.idf_map[orderedQueryList[i][0]]
            cls.tf_idf_map[docs] = store_tf_idf #docs to their tf-idf scores 

        return cls.tf_idf_map
    
if __name__ == "__main__":
    pass

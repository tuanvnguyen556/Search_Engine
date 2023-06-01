from inverted_index import InvertedIndex
from math import log10
class Calculatetfidf:
    """This function calaculates the term frequency and inverted document frequency for each term"""
    idf = dict() #stores the idf of each term
    #of the format: Token (key) : tf-idf (value)

    @classmethod
    def calculate_idf(cls, filename: str):
        """This function will accept a tsv txt file that contains the inverted index
        content and recieve each token. With every recieved token, this function will
        calculate the tf-idf value for each token given the other information that is next to
        the token in the tsv file. the term frequency will be determined from the tsv file, while 
        the document frequency will be recieved from the InvertedIndexDict.
        
        Formula : W [sub(t,d)] = (1 + log(tf [sub(t, d)])) x log(N / df [sub(t)])
        N = total documents
        tf = number of time that t occurs in d -> tsv file 
        df = number of documents that contain t -> frequency in InvertedIndex
        """
        with open(filename) as tsv:
            pass

    def calculate_tf_idf(cls):
        """ All pseudo code, please change later """
        N = InvertedIndex.docID
        
        for k in InvertedIndex.keys():
            # Structure of Inv. Index: {Token: [frequency, [docID, pos1, pos2, ...], [docID2, pos1, pos2, ...], ...]}
            tf_list = [] # TF listing for the current token
            for t in InvertedIndex[k][1:]:
                tf_list.append(len(t) - 1) # the TF of each term is the (len-1) from removing the first docID

            df = int() # TODO
            
            idf[k] = (1 + log(tf)) * log(N / df)

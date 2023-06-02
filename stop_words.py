import json
def stopwords():
    """This function extracts 20 stopwords with the lowest idf value. This will be used for the threshold"""
    #stop is a list of stopwords from the nltk library 
    stop = ["I", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "you're", 
            "you've", "you'll", "you'd", "your", "yours", "yourself", "yourselves", "he", 
            "him", "his", "himself", "she", "she's", "her", "hers", "herself", "it", "it's", 
            "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", 
            "who", "whom", "this", "that","these", "those", "am", "is", "are", "was", "were", "be", 
            "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", 
            "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", 
            "by", "for", "with", "about", "against", "between", "into", "through", "during", 
            "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", 
            "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
              "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", 
                "very", "s", "t", "can", "will", "just", "don", "dont", "should", "now", "d", "ll", 
                "m", "o", "re", "ve", "y", "ain", "aren", "couldn",  "didn",  "doesn",  "hadn", 
                  "hasn",  "haven",  "isn",  "ma", "mightn", "mustn", "needn", "shan" , "shouldn" , 
                  "wasn" , "weren" , "won", "wouldn"]
    with open("idf_scores.json") as f: #finds the idf values for each token
        store_stop = json.load(f) #stores the dict into memory
        store = sorted([(i , store_stop[i.lower()]) for i in stop if i in store_stop], 
                       key=(lambda x: x[1])) #orders the idf from least to greatest
        keep = [store[i][0] for i in range(20)] #retains 20 stopwords for query

if __name__ == "__main__":
    stopwords()
from flask import Flask, render_template, request
import json
import csv
from posting_dictionary import Posting_Dict
from retrieve_from_tsv import getTSVList2 as getTSVList
from tf_idf import Calculatetfidf


app = Flask(__name__) #create app instance

@app.route("/", methods=["POST", "GET"]) #home page
def home():
    if request.method == "GET":
        return render_template("app_index.html") #returns the home page
    else:
        stop_words = ['of', 'and', 'the', 'to', 'a', 'in', 'for', 'is', 'on', 'at', 'with', 'this', 'by', 'that', 'or', 'from', 'are', 'be', 'as', 'an']
        given_query = request.form["query"]
        queryList = list(set(given_query.split()))
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
                orderedQueryList.remove(word)
        if not dict_vals:
            return render_template("redirect_index.html", the_query=given_query,
                                   q1="N/a", q2="N/a", q3="N/a", q4="N/a", q5="N/a")
        else:
            final_urls = sorted([(docs, tf_idf) for docs, tf_idf in \
                                  Calculatetfidf.calculate_tf_idf(dict_vals,orderedQueryList).items()], key=(lambda x: -x[1]))  
            while len(final_urls) <=4 :
                final_urls.append("N/A")
            return render_template("redirect_index.html", the_query=given_query,
                            q1=Posting_Dict.ID_Posting[str(final_urls[0][0])]['url'],
                            q2=Posting_Dict.ID_Posting[str(final_urls[1][0])]['url'],
                            q3=Posting_Dict.ID_Posting[str(final_urls[2][0])]['url'],
                            q4=Posting_Dict.ID_Posting[str(final_urls[3][0])]['url'],
                            q5=Posting_Dict.ID_Posting[str(final_urls[4][0])]['url'])
        
      


if __name__ == "__main__":
    with open("indexer_positions.json") as f1:
        positions_dict = json.load(f1)
        
    # Open posting text file, load the postings content in postingsDict which is also a dictionary structure.
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)
        
    # Open idfScores json file, load the calculated idf into idfMap
    with open("idf_scores.json") as f3:
        Calculatetfidf.idf_map = json.load(f3)
    with open("indexer.tsv", "r") as f:
        file = csv.reader(f, delimiter='\t')
        app.run(debug=True) #automatically reruns web server


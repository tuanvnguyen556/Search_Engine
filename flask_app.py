from flask import Flask, render_template, request
from booleanRetrieval import booleanRetrieval
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
import json
app = Flask(__name__) #create app instance

@app.route("/", methods=["POST", "GET"]) #home page
def home():
    if request.method == "GET":
        return render_template("app_index.html") #returns the home page
    else:
        given_query = request.form["query"]

        retrieve_doc = booleanRetrieval(given_query)
        save_docIDs = retrieve_doc.booleanAndRetrieval()
        display_urls = retrieve_doc.give_url_list(save_docIDs)
        return render_template("redirect_index.html", the_query=given_query) #displays top websites


if __name__ == "__main__":
    with open("indexer.txt") as f1:
        InvertedIndex.InvertedIndexDict = json.load(f1)
    
    with open("posting.txt") as f2:
        Posting_Dict.ID_Posting = json.load(f2)
        
    app.run(debug=True) #automatically reruns web server


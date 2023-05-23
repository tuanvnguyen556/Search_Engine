from flask import Flask, render_template, request
from booleanRetrieval import booleanRetrieval
app = Flask(__name__) #create app instance

@app.route("/", methods=["POST", "GET"]) #home page
def home():
    if request.method == "GET":
        return render_template("app_index.html") #returns the home page
    else:
        given_query = request.form["query"]
        retrieve_doc = booleanRetrieval(given_query)
        save_docIDs = retrieve_doc.booleanAndRetrieval()
        print(save_docIDs)
        return render_template("redirect_index.html", the_query=given_query) #displays top websites


if __name__ == "__main__":
    app.run(debug=True) #automatically reruns web server


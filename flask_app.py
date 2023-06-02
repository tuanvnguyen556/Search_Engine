from flask import Flask, render_template, request

import json

app = Flask(__name__) #create app instance

@app.route("/", methods=["POST", "GET"]) #home page
def home():
    if request.method == "GET":
        return render_template("app_index.html") #returns the home page
    else:
        given_query = request.form["query"]
        return render_template("redirect_index.html", the_query=given_query)
        
      


if __name__ == "__main__":
        
    app.run(debug=True) #automatically reruns web server


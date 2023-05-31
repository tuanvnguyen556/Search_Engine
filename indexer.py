from bs4 import BeautifulSoup
from read_files import read_files
import nltk
from report import make_report
import json
import csv

def index():
    nltk.download('punkt')
    directories = "developer"
    read_files(directories)
    #make_report()

def jsonfied(indexer: dict):

    json_object1 = json.dumps(indexer)
    
    with open("indexer.txt", "w") as json_file1:
        json_file1.write(json_object1)
        json_file1.close()

def jsonfied_posting(posting: dict):
    json_object2 = json.dumps(posting)
    with open("posting.txt", "w") as json_file2:
        json_file2.write(json_object2)
        json_file2.close()



if __name__ == "__main__":
   pass

from bs4 import BeautifulSoup
from read_files import read_files
import nltk
from report import make_report
import json
import csv

def index():
    nltk.download('punkt')
    directories = "C://developer"
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

def tsvfied(indexer: dict):
    #keysToSort = list(indexer.keys())
    
    #keysToSort.sort()
    #print(keysToSort)
    with open("indexer.tsv", "w") as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        #tsv_writer.writerow(["Token", "Frequency", "PositionsMap"])
        for k in indexer.keys():
            tsv_writer.writerow([k, indexer[k][0], indexer[k][1:]])


if __name__ == "__main__":
   pass

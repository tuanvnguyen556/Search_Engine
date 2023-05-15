from bs4 import BeautifulSoup
from read_files import read_files
import nltk
from report import make_report
import json


def index():
    nltk.download('punkt')
    directories = "C://developer"
    read_files(directories)
    make_report()

def jsonfied(indexer: dict):
    json_object = json.dumps(indexer)

    with open("indexer.txt", "w") as json_file:
        json_file.write(json_object)
        json_file.close()

if __name__ == "__main__":
    pass
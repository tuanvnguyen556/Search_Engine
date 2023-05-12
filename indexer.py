from bs4 import BeautifulSoup
from read_files import read_files
import nltk
from report import make_report

def index():
    nltk.download('punkt')
    file = "C://developer"
    read_files(file)
    make_report()
if __name__ == "__main__":
    index()
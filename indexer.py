from read_files import read_files
import nltk
import json


def index():
    '''
    This function begins the indexing
    '''
    nltk.download('punkt') #downloads version to tokenize
    # USER SHOULD CHANGE THIS DIRECTORY TO MATCH THEIR LOCAL DIRECTORY
    directories = "C://developer" 

    read_files(directories) #uses recursion to read the files

def jsonfied(indexer: dict):
    '''
    This function throws the json object of the indexer into a file
    '''
    json_object1 = json.dumps(indexer) #indexer as json object
    
    with open("indexer.txt", "w") as json_file1:
        json_file1.write(json_object1) #passes json object as a txt file
        json_file1.close()

def jsonfied_posting(posting: dict):
    '''
    This function throws the json object of the postings into a file
    '''
    json_object2 = json.dumps(posting) #posting as json object

    with open("posting.txt", "w") as json_file2:
        json_file2.write(json_object2) #passes json object as a txt file
        json_file2.close()

if __name__ == "__main__":
   pass

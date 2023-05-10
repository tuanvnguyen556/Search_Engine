import json

def load_json(given_file):
    open_file = open(given_file, errors='ignore')
    data = json.load(open_file)
    open_file.close()

def run():
    given_file = "C:\\8ef6d99d9f9264fc84514cdd2e680d35843785310331e1db4bbd06dd2b8eda9b.json"
    load_json(given_file)

if __name__ == "__main__":
    run()
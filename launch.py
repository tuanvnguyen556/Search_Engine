import json
import re
from bs4 import BeautifulSoup


def load_json(given_file):
    open_file = open(given_file, errors='ignore')
    try:
        data = json.load(open_file)
        
        soup = BeautifulSoup(data['content'], 'html.parser')
        text = soup.get_text(strip=True)
        textWithoutSymbols = re.sub(r"[^A-Za-z0-9\s]+", "", text)
        print(textWithoutSymbols)
    except:
        pass
    open_file.close()

def run():
    given_file = "C:\\8ef6d99d9f9264fc84514cdd2e680d35843785310331e1db4bbd06dd2b8eda9b.json"
    load_json(given_file)

if __name__ == "__main__":
    run()
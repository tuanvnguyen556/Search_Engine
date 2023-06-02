Final Search_Engine

~INDEXER~

MAKE SURE TO RUN THESE PIP INSTALLS

1. pip install beautifulsoup4
2. pip install --user -U nltk
3. pip install requests
4. pip install flask

BEFORE RUNNING YOUR INDEXER

MAKE SURE TO REMOVE THESE FILES

1. idf_scores.json
2. indexer_positions.json
3. indexer.tsv
4. indexer_path_old.tsv
5. posting.txt

MAKE SURE TO GO INTO indexer.py
TO CHANGE THE LOCATION OF THE developer directory

line 16 should be:

directories variable should be a string path to the developer folder

Finally In order to run the indexer,
you must open up your terminal and run this command

python launch.py

~USER INTERFACE~

if you want a terminal interface

Run this command:

python query.py

if you want a local web interface

Run this command:

python flask_app.py

Info: running query.py and flask_app.py will take some time to load

~Progress~
INDEXER (Milestone 1):
To Convert a text file into a pdf
Use this command on the terminal

pip install aspose-words

To access the tokenizer
Use this command on the terminal

pip install --user -U nltk

To read the html of a website
Use this command on the terminal

pip install beautifulsoup4

To make requests to websites
Use this command on the terminal

pip install requests

To run the user interface
Use this command on the terminal

pip install flask

Overall use these commands to run this program
1. pip install aspose-words
2. pip install beautifulsoup4
3. pip install --user -U nltk
4. pip install requests
5. pip install flask

Make sure to change the directories variable in indexer script
to the path of where the developer folder is located in your system

Finally, navigate to the Search_Engine folder and
run the command on the terminal to run the indexer

python3 launch.py

Query (Milestone 2):
Make sure to make the pip installmenets in the M1
Make sure to change the directories variable in indexer script
to the path of where the developer folder is located in your system

Finally, navigate to the Search_Engine folder and
run the command on the terminal to run the indexer

python3 launch.py

Then, run this command to have a text interface of the query lookup

python3 query.py

To quit the query searchup
Enter this command
quit the query

You will be given the top 5 urls if there are enough urls for 5
otherwise it will give you the top amount the lookup can find


Inverted Index:
object with positions
stashing 1 GB of dict memory into a file
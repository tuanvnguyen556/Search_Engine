import aspose.words
from inverted_index import InvertedIndex
from sys import getsizeof

#aspose is a third-party library that converts text files into pdf
def make_report():
    """
    This function writes into report.txt about data from our Milestone 1
    program. This report file will list out the collaborators, the 
    number of file documents indexed, unique words, and the file size.
    Then this program converts the text file into a readable pdf file.
    """

    #opens the file and writes to report.txt
    with open('report.txt', 'w') as report:
        report.write("Collaborator IDs: 80908952, 51317074, 49766190, 90722907\n")
        report.write(f"*** Here is the data collected from using our indexer ***\n")
        report.write("-" * 57)
        report.write("\n")
        report.write(f"The number of files that were indexed documents is: [{InvertedIndex.docID}]\n")
        report.write(f"The number of unique words is: [{len(InvertedIndex.InvertedIndexDict.keys())}]\n")
        report.write(f"The total size (in KB) of our index on disk is: [{getsizeof(InvertedIndex.InvertedIndexDict)}]\n")
        report.write("-" * 57)
        report.close()
    #creates the pdf
    pdf = aspose.words.Document("report.txt") #load the txt file
    pdf.save("report.pdf", aspose.words.SaveFormat.PDF) #saves the pdf file


if __name__ == "__main__":
    pass
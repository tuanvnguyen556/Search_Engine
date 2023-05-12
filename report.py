import aspose.words

def make_report():
    with open('report.txt', 'w') as report:
        report.write(f"*** Here is the data collected from using our indexer ***\n")
        report.write("-" * 57)
        report.write("\n")
        report.write(f"The number of files that were indexed documents is: [{0}]\n")
        report.write(f"The number of unique words is: [{0}]\n")
        report.write(f"The total size (in KB) of our index on disk is: [{0/1000}]\n")
        report.write("-" * 57)
        report.close()
    pdf = aspose.words.Document("report.txt") #load the txt file
    pdf.save("report.pdf", aspose.words.SaveFormat.PDF)


if __name__ == "__main__":
    make_report()
class InvertedIndex:
    """
    Creates the inverted index for every token in every document.
    Creates a dictionary/map of the token to a list
    where the first index is the frequency of that word and second
    index is the list of documentIDs.
    """
    # Of the format: {"token": [[frequency],[docID1, docID2, ....]]}
    InvertedIndexDict = dict()
    # Start at docID = 1
    docID = 1
    
    @classmethod
    def appendInverted(cls, tokenLst: list):
        """
        This method iterates over the tokenList of tokens and inserts into the dictionary
        frequencyCounter as well as the docID of the current doc. 
        """
        for token in tokenLst:
            # Check if token in dictionary. If not, create new key = token and value = [[frequency = 1],[docID = 1]]
            if token not in cls.InvertedIndexDict:
                cls.InvertedIndexDict[token] = [[1][cls.docID]]
            else:
                # If the token already is in dictioary, check if the current docID is in the docID list.
                # By doing so, we avoid duplicates if the same token is in the same document.
                if cls.docID in cls.InvertedIndexDict[token][1]:
                    pass
                else:
                    # Increament the frequency, and append the new docId in the docID list.
                    cls.InvertedIndexDict[token][0] += 1
                    cls.InvertedIndexDict[token][1] += cls.docID
        # Increment the overall docID
        cls.docID += 1
        
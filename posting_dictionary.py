class Posting_Dict:
    """ Track the Inverted Index and the ID-Posting dictionaries. Should abstract away any adding to these dictionaries."""
    
    ID_Posting = {}

    @classmethod
    def addPosting(cls, docID:int, url, length) -> None:
        """ Given a docID and a posting, this will add it to the dictionary. """

        if docID in cls.ID_Posting: # make sure that this ID does not already exist
            raise KeyError(f"{docID} already exists as a key.")
        
        cls.ID_Posting[docID] = {"url": url, "length": length} # set posting equal to DOC_ID

    def printPosting(self):
        """ Print all urls in the current ID_Posting """
        for i in self.ID_Posting.keys():
            print(self.ID_Posting[i].url)


class InvertedIndex:
    """ Track the Inverted Index and the ID-Posting dictionaries. Should abstract away any adding to these dictionaries."""

    InvertedIndex = {}
    
    ID_Posting = {}

    @classmethod
    def addToInverted(cls, term:str, words: list[tuple]) -> None:
        """ From a single webpage, given a string and a list of words (and their positions), adds to a given term:list[tuple] dictionary where each tuple houses the (Document ID, position in document) """
        
        if cls.InvertedIndex[term]: # append to list
            cls.InvertedIndex[term] += words # add  to end of the term list

        else: # term is not in dictionary, meaning it has never been seen before
            cls.InvertedIndex[term] = words # this word has only been found in this document so far

    @classmethod
    def addPosting(cls, docID:int, posting) -> None:
        """ Given a docID and a posting, this will add it to the dictionary. """

        if docID in cls.ID_Posting: # make sure that this ID does not already exist
            raise KeyError(f"{docID} already exists as a key.")
        
        cls.ID_Posting[docID] = posting # set posting equal to DOC_ID

from posting_dictionary import Posting_Dict
import sys # for writing to file
from indexer import tsvfied
import json

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
    # token : [freq, [docID1, pos1, pos2], [docID2, pos1, pos2], ...]

    terms_to_position = dict()

    @classmethod
    def newAppendInverted(cls, tokenLst: list, data: dict):
        """
        This method iterates over the tokenList of tokens and inserts into the dictionary
        frequencyCounter as well as the docID of the current doc. 
        """
        # Of the format: {"token": [frequency,[docID1, pos1, pos2, ...], [docID2, pos1, pos2, ...]]}
        positionCounter = 1
        token_frequency = {}
        for token in tokenLst:
            # Check if token in dictionary. If not, create new key = token and value = [[frequency = 1],[docID = 1]]
            if token not in cls.InvertedIndexDict:
                cls.InvertedIndexDict[token] = [1,[cls.docID, positionCounter]]
            else:
                # If the token already is in dictioary, check if the current docID is in the docID list.
                # By doing so, we avoid duplicates if the same token is in the same document.
                if cls.docID == cls.InvertedIndexDict[token][-1][0]:
                    cls.InvertedIndexDict[token][-1].append(positionCounter)
                else:
                    # Increment the frequency, and append the new docId in the docID list.
                    cls.InvertedIndexDict[token][0] += 1
                    cls.InvertedIndexDict[token].append([cls.docID, positionCounter])
            if token not in token_frequency:
                token_frequency[token] = 1
            else:
                token_frequency[token] += 1
            positionCounter += 1

        if sys.getsizeof(cls.InvertedIndexDict) > 100000000: # > 100 MB for testing
            cls.write_to_file()
            
        # Increment the overall docID
        Posting_Dict.addPosting(docID=InvertedIndex.docID, url=data['url'], length=len(tokenLst))
        cls.docID += 1
        return token_frequency
    
    @classmethod
    def write_to_file(cls) -> None:
        """ Writes the current inverted_index_dict to a tsv file."""
        new_terms_dict = tsvfied(cls.InvertedIndexDict)
        for key in new_terms_dict:
            if key in cls.terms_to_position:
                cls.terms_to_position[key].append(new_terms_dict[key])
            else:
                cls.terms_to_position[key] = [new_terms_dict[key]]
        
        cls.InvertedIndexDict.clear()

    @classmethod
    def write_positions(cls):
        """ At the end, write the final inverted_index dict to a json file. """
        with open("indexer_positions.json", "w") as f:
            json.dump(cls.terms_to_postition, f)

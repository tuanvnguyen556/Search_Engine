from posting_dictionary import Posting_Dict
import sys # for writing to file
import csv
import json
from pathlib import Path

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
        indexer_path = Path("indexer.tsv")
        positions_path = Path("indexer_positions.json")
        if indexer_path.exists():
            if not positions_path.exists(): # indexer exists but no index positions exist
                raise Exception("Indexer_positions.json does not exist")
            else:
                cls.merge()     
        else:
            new_terms_dict = tsvfied(cls.InvertedIndexDict)
            with open("indexer_positions.json", "w") as f:
                json.dump(new_terms_dict, f)
        
        cls.InvertedIndexDict.clear()

    @classmethod
    def write_positions(cls):
        """ At the end, write the final inverted_index dict to a json file. """
        with open("indexer_positions.json", "a") as f:
            json.dump(cls.terms_to_postition, f)

    @classmethod
    def merge(cls):
        """ Binary merge on a file if it """
        indexer_path = Path("indexer.tsv")
        positions_path = Path("indexer_positions.json")
        with open("indexer_positions.json") as pos_dict:
            prev_positions = json.load(pos_dict)
            indexer_path.rename(Path("indexer_path_old.tsv")) # make the old file indexer_path_old.tsv
            with open("indexer_path_old.tsv") as old:
                with open("indexer.tsv", "w") as curr:
                    tsv_writer = csv.writer(curr, delimiter='\t', lineterminator='\n')
                    new_positions = {}
                    for term in prev_positions: # loop through all terms currently in the tsv file
                        old.seek(prev_positions[term]) # f.seek(position)
                        line = old.readline().split('\t')
                        #print(line)
                        try:
                            freq = int(line[1])
                        except:
                            print(line)
                            raise Exception()
                        lst_positions = [json.loads(line[i]) for i in range(2, len(line))] # correctly gets [Token, Frequency(int), *positions(lst)]
                        if term in cls.InvertedIndexDict: # if more data to append
                            freq += cls.InvertedIndexDict[term][0] # add to the frequency
                            for i in range(1, len(cls.InvertedIndexDict[term])):
                                lst_positions.append(cls.InvertedIndexDict[term][i]) # append all found positions
                        
                        new_positions[term] = curr.tell() # get file position
                        tsv_writer.writerow([term, freq, *lst_positions])
                    
                    for term in cls.InvertedIndexDict: # add all new terms
                        if term in new_positions: 
                            continue # skip term if it has already been added
                        else: # term doesn't currently exis
                            new_positions[term] = curr.tell()
                            tsv_writer.writerow([term, cls.InvertedIndexDict[term][0], *cls.InvertedIndexDict[term][1:]])
        with open("indexer_positions.json", "w") as new_pos_file: # write new positions to new index file
            json.dump(new_positions, new_pos_file)

def tsvfied(indexer: dict):
    """This writes the inverted index as a tsv file for optimizing query time"""
    with open("indexer.tsv", "w") as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n') 
        terms_dict = {}
        for k in indexer.keys():
            terms_dict[k] = tsv_file.tell() # tells us the index position
            tsv_writer.writerow([k, indexer[k][0], *indexer[k][1:]])
    
    return terms_dict

def positions(pos : dict, qlist: list) -> bool:
    """This function ensures that the the order of the query matches
    a segment within a url"""
    pass

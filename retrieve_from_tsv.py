import json
import csv

# defunct
def getTSVList(f: csv.reader, q: str, pos: int)->list:
    """ Given a file, query word, and position, return the corresponding line"""
    f.seek(pos)
    line = f.readline().split('\t')
    return [json.loads(line[i]) for i in range(2, len(line))]

# this is what we use
def getTSVList2(f: csv.reader, q: str, pos: int, dict_IDs: dict, maxKey: int = 0): # dict_IDs: {1:[[1, 2, 3, 4], [1, 5, 6]]}
    """ Given a file, query word, and position, and set, return the corresponding line."""
    f.seek(pos)
    line = f.readline().split('\t')
    dict_results = {}
    if not dict_IDs: # empty, need to create a dictionary of possible docIDs
        min_val = min(len(line), 10000) # cap at 10000 (slightly less than half corpus) if the word has high count 
        for i in range(2, min_val):
            lst_positions = json.loads(line[i])
            currKey = lst_positions[0]
            dict_results[currKey] = [lst_positions]
        return dict_results, currKey # {1: [[]], 3: [[]]}
    else:
        dict_results = {} # r
        for i in range(2, len(line)):
            lst_positions = json.loads(line[i]) # [1, 2, 4, 5] loads a list
            currKey = lst_positions[0] # [2, 1, 3]
            if currKey > maxKey:
                break # no need to read more
            if currKey in dict_IDs: # current docID also was in the previous dictionary, so we want to add this key (and the corresponding lists) to the dictionary of possible documents
                dict_results[currKey] = dict_IDs[currKey] 
                dict_results[currKey].append(lst_positions)
            else:
                continue
        return dict_results, currKey # return the maximum key reached (highest docID, so that future calls can stop iteration early), and dictionary of corresponding documents (to lists of token positions)

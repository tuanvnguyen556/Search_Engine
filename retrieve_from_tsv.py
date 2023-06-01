import json
import csv

def getTSVList(f: csv.reader, q: str, pos: int)->list:
    """ Given a file, query word, and position, return the corresponding line"""
    f.seek(pos)
    line = f.readline().split('\t')
    return [json.loads(line[i]) for i in range(2, len(line))]
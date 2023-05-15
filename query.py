""" Run this file and enter a query from the terminal. """

import sys
import inverted_index

def main() -> None:
    if len(sys.argv) == 1: # no query
        raise Exception("Please enter a query.")
    query = [term.lower() for term in sys.argv[1:]]
    for term in query:
        if term not in inverted_index.InvertedIndex:
            print(f"Term {term} has no search results.") # boolean AND: term doesn't exist, we can't really return any results
            return None # break out of function

    # lst_doc_IDs = some_intersection_function(*[inverted_index.InvertedIndex[term] for term in query])
    # printer(doc_IDs)
    

    

if __name__ == "__main__":
    main()
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
class booleanRetrieval:
    """
    This class operates different booleanRetrieval models from the indexer created in milestone 1.
    """
    def __init__(self):
        # self.queryList = query.split()
        self.top_urls = []
    
    
    # A helper function which finds the intersection between two given lists
    def listIntersection(self, givenList: list, commonList: list):
        # givenList = [[1, 1, 3], [2, 1, 2], [3, 1, 2, 3]]
        # commonList = [[1, 1, 2], [2, 1, 3]]
        # Should return: [1, 2]
        docIDLst1 = [lst[0] for lst in givenList]
        docIDLst2 = [lst[0] for lst in commonList]
        return [item for item in docIDLst1 if item in docIDLst2]


    # The booleanAndRetrieval finds the AND intersection between the provided queries.
    def booleanAndRetrieval(self, query: str, *docIDLists: list):
        # Check if the query is empty
        if len(docIDLists) == 0:
            return []
        # Check if the query is in the dictionary
        if len(query.split()) != len(docIDLists): 
            return []
        
        # Initialize a commonList which contains the docIDs of the first token
        commonList = []
        for lst in docIDLists[0]:
            commonList.append(lst[0])
            
        # If there is only one query, retyurn the list of docIDs
        # docIDLists = [[[1, 1, 3], [2, 1, 2], [3, 1, 2, 3]]]
        if len(docIDLists) == 1: return commonList
        
        # Otherwise, run the intersection algorithm for the rest of the lists within the docIDLists
        # docIDLists = [[[1, 1, 3], [2, 1, 2], [3, 1, 2, 3]], [[1, 1, 2], [2, 1, 3]]]
        for lst in docIDLists[1:]:
            commonList = self.listIntersection(lst, commonList)
            
        # Return the final list of common documents
        return commonList
            
    def return_query(self):
        return self.queryList
    
    def print_urls(self, commonList: list):
        if len(commonList) == 0:
            print(f"Try changing your query request. No documents were found with the provided query.\n")
        elif len(commonList) == 1:
            if commonList[0] in Posting_Dict.ID_Posting.keys():
                print(f"Here is a url of interest: {Posting_Dict.ID_Posting[commonList[0]]['url']}\n")
        else:
            best_urls = {}
            for i in commonList:
                if str(i) in Posting_Dict.ID_Posting.keys():
                    counter = 0 
                    for tok, freq in Posting_Dict.ID_Posting[str(i)]['content'].items():
                        if tok in self.queryList:
                            counter += freq
                    best_urls[i] = counter
            display_urls = sorted([(hashing, frequencies)for hashing, frequencies in best_urls.items()], key= (lambda x: -x[1]))
            for hash in range(5):
                if hash not in range(len(display_urls)):
                    break
                else:
                    print(f"Here is a url of interest: {Posting_Dict.ID_Posting[str(display_urls[hash][0])]['url']}")
    
    def give_url_list(self, commonList):
        if len(commonList) == 0:
            return []
        elif len(commonList) == 1:
            if commonList[0] in Posting_Dict.ID_Posting.keys():
                return [Posting_Dict.ID_Posting[commonList[0]]['url']]
        else:
            best_urls = {}
            for i in commonList:
                if str(i) in Posting_Dict.ID_Posting.keys():
                    counter = 0 
                    for tok, freq in Posting_Dict.ID_Posting[str(i)]['content'].items():
                        if tok in self.queryList:
                            counter += freq
                    best_urls[i] = counter
            return sorted([(hashing, frequencies)for hashing, frequencies in best_urls.items()], key= (lambda x: -x[1]))
            

        
    
from inverted_index import InvertedIndex
from posting_dictionary import Posting_Dict
class booleanRetrieval:
    """
    This class operates different booleanRetrieval models from the indexer created in milestone 1.
    """
    def __init__(self, query: str):
        self.queryList = query.split()
        self.top_urls = []
    # The booleanAndRetrieval finds the AND intersection between the provided queries.
    def booleanAndRetrieval(self):        
        for i in self.queryList:
            if i not in InvertedIndex.InvertedIndexDict.keys():
                return []
        if len(self.queryList) == 1:
            return InvertedIndex.InvertedIndexDict[self.queryList[0]][1]
        
        # Initialize a commonList which contains the common elements from the list of docIDs
        # corresponding to the given queries
        queryList = sorted([InvertedIndex.Dict[key] for key in query], key=len)
        commonList = self.listIntersection(queryList[0], queryList[1])
        # commonList = self.listIntersection(InvertedIndex.InvertedIndexDict[queryList[0]][1], InvertedIndex.InvertedIndexDict[queryList[1]][1])
        
        # If the query only asks for the intersection of two words, then return the current commonList
        if len(self.queryList) == 2:
            return commonList
        
        # Otherwise, find the commonList with every other list corresponding to every other
        # query other than the first 2 queries in the queryList.
        for index in range(2, len(queryList)):
            #commonList = self.listIntersection(InvertedIndex.InvertedIndexDict[queryList[index]][1], commonList)
            commonList = self.listIntersection(queryList[index], commonList)

        # Return the final list of common documents
        return commonList
            
    def return_query(self):
        return self.queryList
    # A helper function which finds the intersection between two given lists
    def listIntersection(self, givenList: list, commonList: list):
        return [item for item in givenList if item in commonList]
    
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
            

        
    
from inverted_index import *

class booleanRetrieval:
    """
    This class operates different booleanRetrieval models from the indexer created in milestone 1.
    """
    
    # The booleanAndRetrieval finds the AND intersection between the provided queries.
    def booleanAndRetrieval(self, query: str):
        queryList = query.split()
        
        for token in queryList:
            if token not in InvertedIndex.InvertedIndexDict.keys():
                return []
            
        if len(queryList) == 1:
            return InvertedIndex.InvertedIndexDict[queryList[0]][1]
        
        # Initialize a commonList which contains the common elements from the list of docIDs
        # corresponding to the given queries
        queryList = sorted([InvertedIndex.Dict[key] for key in query], key=len)
        commonList = self.listIntersection(queryList[0], queryList[1])
        # commonList = self.listIntersection(InvertedIndex.InvertedIndexDict[queryList[0]][1], InvertedIndex.InvertedIndexDict[queryList[1]][1])
        
        # If the query only asks for the intersection of two words, then return the current commonList
        if len(queryList == 2): return commonList
        
        # Otherwise, find the commonList with every other list corresponding to every other
        # query other than the first 2 queries in the queryList.
        for index in range(2, len(queryList)):
            #commonList = self.listIntersection(InvertedIndex.InvertedIndexDict[queryList[index]][1], commonList)
            commonList = self.listIntersection(queryList[index], commonList)
        
        # Return the final list of common documents
        return commonList
            
    
    # A helper function which finds the intersection between two given lists
    def listIntersection(self, givenList: list, commonList: list):
        return [item for item in givenList if item in commonList]
    
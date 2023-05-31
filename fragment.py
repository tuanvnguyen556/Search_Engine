class Remove_fragments:
    '''
    This class will remove fragments from url's since
    fragments are separate sections within the same url.
    This filtering mechanism only stores unique urls
    within the inverted index
    '''
    unique_urls = set() #stores the unique urls

    @classmethod #decorator to save the state of the class until the program ends
    def remove_fragment(cls, given_url: str) -> str:
        unique_url = given_url[:given_url.find('#')] #strips the fragment from the url
        if unique_url not in cls.unique_urls:
            cls.unique_urls.add(unique_url) #stores the unique url so that it has been counted
            return unique_url  
            #returns true for the inverted indexer to know that the passed url has not been processed yet
        else:
            return '' #empty string as a falsy value for boolean if statement
            
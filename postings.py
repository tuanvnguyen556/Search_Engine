from dataclasses import dataclass

@dataclass
class Posting:
    """ Contains information about the website that will be stored in the posting."""

    url: str
    encoding: str
    content: str

class docID_counter:
    """ Contains the current docID. Increment for each document, prior to processing the document (initializes at 0,
    but we want the first document's ID to be 1.)"""

    docID = 0

    @classmethod
    def increment(cls): # increment the ID
        cls.docID+=1
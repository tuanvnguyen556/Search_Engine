class InvertedIndex2:
    InvertedIndex2 = dict()
    # Of the format: {"token": [[frequency],[docID1, docID2, ....]]}
    docID = 1
    
    @classmethod
    def appendInverted(cls, tokenLst: list):
        for token in tokenLst:
            if token not in cls.InvertedIndex2:
                cls.InvertedIndex2[token] = [[1][cls.docID]]
            else:
                if cls.docID in cls.InvertedIndex2[token][1]:
                    pass
                else:
                    cls.InvertedIndex2[token][0] += 1
                    cls.InvertedIndex2[token][1] += cls.docID
        cls.docID += 1
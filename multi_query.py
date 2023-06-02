def kevin_multi_query(sentence, tsv_file, orderedList) -> dict:
    """
    Scuffed sentence finder with no efficiency. Linear search without accounting for weighting

    sentence: query
    tsv_file: map of tokens to list of lists, discard frequiency since not needed

    """


    d = {sent:[] for sent in sentence}
    for id in tsv_file:
        for i in range(len(tsv_file[id])):
            d[orderedList[i][0]].append(tsv_file[id][i])
    
    tsv_file = d


    # {docID: [[], [], []]}
    # {token: [[], [], []]}
    result = {} # return value of format {docID : times sentence appears}


    for doc in tsv_file[sentence[0]]:
        # Loop through all [docID, pos, pos, pos] containing the first word
        # TODO: use continue if docID does not contain all words

        sentence_map = [doc[1:]] # List of lists

        for next_word in sentence[1:]:
        # Attempt to build a complete sentence map
        
            for d in tsv_file[next_word]:
                # Find and add the [docID, pos, pos] with same docID as doc
                if d[0] == doc[0]:
                    sentence_map.append(d[1:])

        if len(sentence_map) < len(sentence):
            # Skip if entire query does not appear in the current docID
            print(len(sentence_map))
            continue
            

        for p in sentence_map[0]:
            # Iterate through first word's [pos1, pos2, pos3] and look for consecutive pos in the other docIDs
            sentence_found = True
            npos = p+1 # Expected position of next token

            for d in sentence_map[1:]:
                if npos not in d:
                    sentence_found = False
                else:
                    npos += 1

            if sentence_found:
                if doc[0] in result.keys():
                    result[doc[0]] += 1
                else:
                    result[doc[0]] = 1

    return result




import os
from process import file_processor
import inverted_index 

def read_files(filename) -> None:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist as a relative nor absolute path.")
        # raise an error if this file doesn't exist
    
    for file in os.listdir(filename):
        full_relative = os.path.join(filename, file)

        if os.path.isdir(full_relative): # must iterate through a subdirectory
            read_files(full_relative)
        else: # if not a folder, must be a file
            # some pipeline function to process the file
            tokenList, code = file_processor(full_relative)
            if code:
                start = inverted_index.InvertedIndex()
                start.appendInverted(tokenList, code)
            
            


if __name__ == "__main__":
    pass

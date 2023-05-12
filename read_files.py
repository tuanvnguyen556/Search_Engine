import os
from process import file_processor

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
            store = file_processor(full_relative)
            print(store)


if __name__ == "__main__":
    given_file = "C:\\Store"
    read_files(given_file)

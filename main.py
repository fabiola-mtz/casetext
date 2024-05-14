from file_input_handling import read_files_in_directory

if __name__ == "__main__":
    FILES_DIR = '/content'
    # INPUT: SAMPLE FILES
    files = read_files_in_directory(FILES_DIR)
    #print (len(files))
    # Prtinting only
    for file_text in files:
      print("File:", file_text[0])
      print("Text:")
      print(file_text)
    # OUTPUT: INFORMATIVE TEXT

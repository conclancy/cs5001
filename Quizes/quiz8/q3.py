def read_file(file_path):
    '''
    read_file takes in a file path as a string, opens the file for reading
    and prints the contents of the file.
    params: string path to file location
    returns: None
    '''

    # open the file
    file = open(file_path, "r")

    # print file contents
    print(file.read())

    # close the file
    file.close()

read_file("/Users/cclancy/Documents/personal/cs5001/Quizes/quiz8/test_file.txt")
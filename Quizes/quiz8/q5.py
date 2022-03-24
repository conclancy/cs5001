def file_writer():
    '''
    file_writer adds "I can code in Python!" to a file supplied by the caller
    params: None
    returns: None
    '''

    # create loop variable
    alive = True

    while alive:
        
        try:

            # take in file path
            file_path = input("Enter file path:")

            # open the file for appending
            file = open(file_path, "a")

            # write new line to file
            file.write("\nI can code in Python!")

            # close the file
            file.close()

            # open the file for reading
            file = open(file_path, "r")

            # print file contents
            print(file.read())

            # close the file
            file.close()

            # ends program
            alive = False

        except Exception as e:
            print(e, "\n Please enter a valid file path")

file_writer() 

# read_file("/Users/cclancy/Documents/personal/cs5001/Quizes/quiz8/test_file.txt")
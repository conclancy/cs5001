def main():
    '''
    read_file promts the caller for  a file path as a string, opens the file
    for reading and prints the contents of the file.
    params: None
    returns: None
    '''

    alive = True

    while alive:
        try:

            # take in file path
            file_path = input("Enter file path:")

            # open the file
            file = open(file_path, "r")

            # print file contents
            print(file.read())

            # close the file
            file.close()

            # ends program
            alive = False

        except Exception as e:
            print(e, "\n Please enter a valid file path")

main() 

# read_file("/Users/cclancy/Documents/personal/cs5001/Quizes/quiz8/test_file.txt")
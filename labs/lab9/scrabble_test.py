from scrabble import * 

words = {}

test = read_text_file()

dictionary = store_words(test)


print(dictionary[2][:5])
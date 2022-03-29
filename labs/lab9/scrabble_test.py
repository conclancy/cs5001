from scrabble import * 


words = {}

test = read_text_file()

dictionary = store_words(test)

print(get_words(4, dictionary, "for"))
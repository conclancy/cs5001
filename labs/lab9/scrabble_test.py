from scrabble import * 


test = read_text_file()

dictionary = store_words(test)

words = get_words(4, dictionary, "for")

print(get_scores(words))
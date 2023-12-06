def print_upper_words(word_list):
    # Go through list of words and return all in uppercase on separate lines
    # word_list: The list of words to return ["a", "b", "c"]
    output = ""
    for word in word_list:
        output += word.upper() + "\n"
    return output

print("PRINT UPPER WORDS")
print(print_upper_words(["hello", "hey", "goodbye", "yo", "yes"]))

def printWordsStartingWithE(word_list):
    # Go through list of words and return all in uppercase on separate lines
    # word_list: The list of words to return ["a", "b", "c"]

    output = ""
    for word in word_list:
        word = word.upper()
        if('E' in word):
            output+= word + "\n"
    return output

print("PRINT WORDS STARTING WITH E" + "\n" + printWordsStartingWithE(["eyy", "hey", "goodbye", "eyo", "yes"]))


def printWordsWithLetters(word_list, letter_list):
    output = ""

    for letter in letter_list:
        letter = letter.upper()
    
    for word in word_list:
        word = word.upper()
        if(word[0] in letter_list):
            output+= word + "\n"
    return output

print("PRINT WORDS WITH LETTERS" + "\n" + printWordsWithLetters(["Apple", "Banana", "Coconut", "Quandong"], ["A", "B", "C"]))

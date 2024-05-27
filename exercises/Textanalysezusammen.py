def enter_text():
    return input("Please enter a text:\n>")

#wortzählung

def word_count(text):
    # remove punctuation and make the text lowercase
    text = text.lower()
    for char in "-.,\n":
        text = text.replace(char, ' ')
    words = text.split
    return len(words), words

def word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency                

def longest_word(words):
    max_word = ""
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word



text = enter_text()
#print(word_count(text))
print(longest_word(text))
#print(word_frequency(text))



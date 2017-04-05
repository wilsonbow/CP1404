
user_text = input("Text: ")
words = {}

user_text_words = user_text.split(' ')
for word in user_text_words:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for word in words:
    print("{}: {}".format(word, words[word]))


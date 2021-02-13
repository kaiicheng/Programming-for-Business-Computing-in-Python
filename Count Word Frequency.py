sentence = input().split(" ")
word_freq = dict()
print(sentence)

for i in range(len(sentence)):
    # print("sentence[i]:", sentence[i])
    # Punctuation marks only appear after word, and only one at a time.
    word = sentence[i].strip(",.:;!?")   ################3
    # print("word:", word)

    if word == "":
        continue
    word = word.lower()

    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

print("word_freq:", word_freq)

max_freq = -1
max_word = ""
for word in word_freq:
    freq = word_freq[word]
    # print("word:", word)
    if freq > max_freq or (freq == max_freq and word < max_word):
        # print("word:", word)
        max_freq = freq
        max_word = word

print(max_word + "," + str(max_freq))

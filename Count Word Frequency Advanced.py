sentence = input().split(" ")
ignore = input().split(",")
word_freq = dict()
print(sentence)

for i in range(len(ignore)):
    ignore[i] = ignore[i].lower()


for i in range(len(sentence)):
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
    if word in ignore:
        print("ignore:", ignore)
        continue  ###### Skip code below in this loop and continue next loop.
    freq = word_freq[word]
    print("word:", word)
    if freq > max_freq or (freq == max_freq and word < max_word):
        # print("word:", word)
        max_freq = freq
        max_word = word

if max_freq >= 0:
    print(max_word + "," + str(max_freq))
else:
    print("-1")
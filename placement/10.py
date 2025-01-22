# Using a dictionary to store word frequencies
word_freq = {}
for word in ["apple", "banana", "apple"]:
    word_freq[word] = word_freq.get(word, 0) + 1

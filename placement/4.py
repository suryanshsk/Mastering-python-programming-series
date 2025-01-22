# Question: Write a function to count the occurrences of each word in a sentence.
def word_count(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

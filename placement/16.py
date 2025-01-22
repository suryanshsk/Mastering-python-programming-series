# Question: Implement a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

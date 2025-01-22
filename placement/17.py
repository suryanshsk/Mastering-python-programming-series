# Question: Write a function to find the longest palindromic substring in a given string.
def longest_palindrome(s):
    if len(s) == 0:
        return ""
    longest = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest

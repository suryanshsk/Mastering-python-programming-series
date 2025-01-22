import re

text = "The quick brown fox jumps over the lazy dog"
pattern = r"quick"
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())

import re
text = "Contact me at suryanshsk@hotmail.com"
pattern = r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b"
email = re.findall(pattern, text)
print("Extracted email:", email)

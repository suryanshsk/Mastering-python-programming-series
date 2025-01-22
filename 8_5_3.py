import re
text = "The rain in Spain"
new_text = re.sub(r"ain", "XYZ", text)
print("Replaced text:", new_text)

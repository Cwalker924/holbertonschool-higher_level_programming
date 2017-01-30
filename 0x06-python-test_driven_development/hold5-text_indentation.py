"""
This module holds only one function:
text_indentation()
"""

def text_indentation(text):
    delim = [".", "?", ":"]
    typeError = ["text must be a string"]

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    new_string = ""
    for word in text.split("\n"):
        n = ("\n".join([word.strip()]))
    print(n, end="")

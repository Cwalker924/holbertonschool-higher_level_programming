#!/usr/bin/python3
"""
This module holds only one function:
text_indentation()
"""


def text_indentation(text):
    typeError = "text must be a string"

    if isinstance(text, str) is False:
        raise TypeError(typeError)

    if text is None:
        raise TypeError(typeError)

    if len(text) < 0:
        raise TypeError(typeError)

    sent = text.split()
    for word in sent:
        if word[-1] in ".?:":
            print(word, end="")
            print("")
            print("")
        else:
            print(word, end=" ")
    print("")

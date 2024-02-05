#!/usr/bin/python3
"""this module prints a text"""


def text_indentation(text):
    """this defines it"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    current_sentence = ""

    for char in text:
        if char in ".?:":
            sentences.append(current_sentence.strip() + char)
            current_sentence = ""
        else:
            current_sentence += char

    if current_sentence:
        sentences.append(current_sentence.strip())

    for sentence in sentences:
        print(sentence + "\n")
    print(sentence, end="")

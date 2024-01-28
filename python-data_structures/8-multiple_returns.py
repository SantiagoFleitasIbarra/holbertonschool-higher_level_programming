#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    length = len(sentence)
    character = sentence[0]
    return(length, character)
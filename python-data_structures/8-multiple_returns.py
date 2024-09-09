#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(0, len(sentence)):
        return (len(sentence), sentence[0])

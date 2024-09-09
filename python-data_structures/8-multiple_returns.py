#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(0, len(sentence)):
        if i == 0:
            return None
        else:
            return (len(sentence), sentence[0])

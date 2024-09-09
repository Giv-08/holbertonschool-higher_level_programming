#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(0, len(sentence)):
        if len(sentence) == 0:
            return (0, None)
        else:
            return (len(sentence), sentence[0])

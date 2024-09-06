#!/usr/bin/python3
alphabets = [chr(a) for a in range(65, 91)]

sorted_alphabets = sorted(alphabets, reverse=True)
result = ""
for i in sorted_alphabets:
        if ord(i) % 2 == 0:
            result += i.lower()
        else:
            result += i
print("{}".format(result))

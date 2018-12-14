import numpy as np


def checksum(data):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = 0
    y = 0
    for i,boxid in enumerate(data):
        counter = {letter: 0 for letter in alphabet}
        for char in boxid: 
            counter[char] += 1
        for letter in alphabet: 
            if counter[letter] == 2:
                x += 1
                break
        for letter in alphabet: 
            if counter[letter] == 3:
                y += 1
                break
    return x * y


def correct_boxes(data):
    for i, box1 in enumerate(data):
        for j, box2 in enumerate(data):
            if i == j: 
                continue
            else: 
                diff = 0
                for char1, char2 in zip(box1, box2): 
                    if char1 != char2: 
                        diff += 1
                if diff == 1:
                    return [box1, box2]

def common_letters(data):
    b1, b2 = correct_boxes(data)
    code = ""
    for c1,c2 in zip(b1, b2):
        if c1 == c2:
            code += c1
    return code


if __name__ == "__main__":
    data = np.loadtxt("input", dtype=str)
    print(checksum(data))
    print(common_letters(data))

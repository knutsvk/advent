from collections import defaultdict
import numpy as np


def get_input():
    with open("input") as inputfile: 
        data = inputfile.readline()
    return data


def reduce(polymer):
    something_changed = True
    n = len(polymer)-1
    while(something_changed):
        # Keep going over the (smaller and smaller) polymer until it doesnt change
        something_changed = False
        i = 0
        while(i < n-2):
            while (polymer[i+1] != polymer[i]) & \
                    (polymer[i+1] == polymer[i].upper() or polymer[i+1] == polymer[i].lower()):
                polymer = polymer[:i] + polymer[i+2:]
                something_changed = True
                n = len(polymer)-1
            i += 1
    return n


def improve(polymer):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    counter = {letter: 0 for letter in alphabet}
    for letter in alphabet:
        polymer_without_letter = polymer.replace(letter, '')
        polymer_without_letter = polymer_without_letter.replace(letter.upper(), '')
        counter[letter] = reduce(polymer_without_letter)
    return min(counter.values()) 


if __name__ == "__main__":
    polymer = get_input()
    print(reduce(polymer))
    print(improve(polymer))

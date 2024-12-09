from math import log10
from sys import stdin

def entropy(Lambda, words):
    som = 0
    for count in words.values():
        som += count * (log10(Lambda) - log10(count))
    return 1 / Lambda * som

def process_input():
    specials = [",", ".", ":", ";", "!", "?", "\"", "(", ")"]
    line = stdin.readline().strip()
    words = {}
    Lambda = 0

    while line != "****END_OF_INPUT****":
        if line != "****END_OF_TEXT****":
            line = line.lower()
            for char in specials:
                line = line.replace(char, "")
            line = line.split()
            for word in line:
                Lambda += 1
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
        else:
            ent = entropy(Lambda, words)
            emax = log10(Lambda)
            rel_ent = ent / emax * 100
            print(f"{Lambda} {ent:.1f} {rel_ent:.0f}")
            Lambda = 0
            words = {}

        line = stdin.readline().strip()

def main():
    process_input()

if __name__ == "__main__":
    main()

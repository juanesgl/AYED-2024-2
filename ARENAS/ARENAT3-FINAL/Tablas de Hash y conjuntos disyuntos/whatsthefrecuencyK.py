from sys import stdin
from collections import defaultdict

def process_line(line):
    letter_count = defaultdict(int)  
    max_frequency = 0               

    for character in line:
        if character.isalpha():  
            letter_count[character] += 1
            if letter_count[character] > max_frequency:
                max_frequency = letter_count[character]

    most_frequent_letters = []
    for letter in sorted(letter_count):  
        if letter_count[letter] == max_frequency:
            most_frequent_letters.append(letter)

    if max_frequency > 0:
        print("".join(most_frequent_letters), max_frequency)

def main():
    
    for line in stdin:
        process_line(line.strip())  

if __name__ == "__main__":
    main()

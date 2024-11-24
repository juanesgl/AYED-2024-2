from sys import stdin

def main():
    words = int(stdin.readline().strip())  # Convert input to integer
    for i in range(words):
        word = stdin.readline().strip()  # Use stdin for reading words
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)

main()

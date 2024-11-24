from sys import stdin

def calculate_payment(k_characters, article):
    total_value = 0
    for line in article:
        for char in line:
            if char in k_characters:
                total_value += k_characters[char]
    return total_value / 100

def main():
    lines = int(stdin.readline().strip())
    if not (0 < lines <= 5):  
        return
    
    for _ in range(lines):
        K = int(stdin.readline().strip())
        k_characters = {}
        for _ in range(K):
            character, value = stdin.readline().split()
            k_characters[character] = int(value)

        M = int(stdin.readline().strip())
        article = [stdin.readline().strip() for _ in range(M)]

        payment = calculate_payment(k_characters, article)
        print(f"{payment:.2f}$")

if __name__ == "__main__":
    main()
    
from sys import stdin

def decrypt_message(encrypted_text):
    length = len(encrypted_text)  

    rows, cols = 1, length  
    for i in range(1, int(length ** 0.5) + 1): 
        if length % i == 0:  
            c = length // i
            if i <= c:
                rows, cols = i, c  
    matrix = [[''] * cols for _ in range(rows)]  # Crear la matriz
    idx = 0

    for col in range(cols): 
        for row in range(rows):
            matrix[row][col] = encrypted_text[idx]
            idx += 1  

    decrypted_text = ''.join(''.join(row) for row in matrix) 
    return decrypted_text

def main():
    line = stdin.readline().strip()
    while line:
        if len(line) < 101:
            result = decrypt_message(line)
            print(result)
        line = stdin.readline().strip()

main()
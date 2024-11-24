from sys import stdin

def is_quirksome(num):
    n = len(str(num))
    half_num = n // 2
    num_str = str(num).zfill(n)
    first_part = int(num_str[:half_num])
    second_part = int(num_str[half_num:])
    suma_de_partes = first_part + second_part
    cuadrados = suma_de_partes**2
    return str(cuadrados).zfill(n) == num_str

def main():
    # Pre-calculate quirksome squares up to a reasonable limit
    quirksome_squares = set(n**2 for n in range(10**4))  # Adjust limit as needed

    digit = [int(line.strip()) for line in stdin]
    for n in digit:
        # Calculate minimum and maximum possible quirksome squares for n digits
        min_square = 10**(n-1)
        max_square = 10**n - 1

        # Iterate only over the possible range of quirksome squares
        for num in quirksome_squares:
            if min_square <= num <= max_square:
                print(f"{num:0{n}d}")
main()
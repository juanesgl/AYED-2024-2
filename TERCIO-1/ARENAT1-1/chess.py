from sys import stdin 

def max_rows(n):
    # Calculamos un valor inicial para high basándonos en la estimación
    low, high = 1, int(2 * (n ** 0.5)) + 1  
    while low <= high:
        mid = (low + high) // 2
        total_warriors = mid * (mid + 1) // 2  # Calculamos la suma de los primeros mid números
        
        if total_warriors <= n:
            low = mid + 1  # Si podemos formar esta cantidad de filas, intentamos con más
        else:
            high = mid - 1  # Si no podemos, intentamos con menos
    
    return high

def main():
    input = stdin.read()
    data_entry = input().splitlines()
    number_of_test_cases = int(data_entry[0])  # Número de casos de prueba
    results = []

    for i in range(1, number_of_test_cases + 1):
        number_of_warriors = int(data_entry[i])
        results.append(max_rows(number_of_warriors))

    for result in results:
        print(result)

main()
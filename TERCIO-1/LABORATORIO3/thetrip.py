import sys
import math

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    index = 0
    while index < len(data):
        # Leer el número de estudiantes
        N = int(data[index].strip())
        index += 1
        
        if N == 0:
            break
        
        # Leer los gastos de los estudiantes
        total_cents = 0
        expenses = []
        
        for _ in range(N):
            dollar, cent = map(int, data[index].strip().split('.'))
            expense_in_cents = dollar * 100 + cent
            expenses.append(expense_in_cents)
            total_cents += expense_in_cents
            index += 1
        
        # Calcular el promedio
        low_average = total_cents // N
        high_average = low_average + (1 if total_cents % N != 0 else 0)
        
        # Calcular el total de dinero que debe intercambiarse
        sum_above = sum(expense - high_average for expense in expenses if expense > high_average)
        sum_below = sum(low_average - expense for expense in expenses if expense < low_average)
        
        used_sum = max(sum_above, sum_below)
        
        # Imprimir el resultado en formato adecuado
        print(f"${used_sum // 100}.{used_sum % 100:02d}")

main()
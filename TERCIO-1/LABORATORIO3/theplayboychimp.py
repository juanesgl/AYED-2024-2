from sys import stdin
import bisect 
def main():
    chimpances_row = int(stdin.readline().strip())
   
    chimpances_heights = list(map(int, stdin.readline().strip().split()))
   
    number_of_queries = int(stdin.readline().strip())
    
    luchu_heights = list(map(int, stdin.readline().strip().split()))

    for luchu_height in luchu_heights:
        # Buscar la posición para insertar la altura de Luchu en la lista de alturas de chimpancés
        lower_index = bisect.bisect_left(chimpances_heights, luchu_height) - 1
        upper_index = bisect.bisect_right(chimpances_heights, luchu_height)

        # Determinar la altura menor
        if lower_index >= 0:
            lower = chimpances_heights[lower_index]
        else:
            lower = 'X'
        
        # Determinar la altura mayor
        if upper_index < chimpances_row:
            upper = chimpances_heights[upper_index]
        else:
            upper = 'X'
        
        # Imprimir la respuesta para esta altura de Luchu
        print(lower, upper)
        
main()
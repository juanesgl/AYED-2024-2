from sys import stdin

def movement_calculaction(bins, colors):
    total_movements = 0
    
    # Mapear colores a índices
    color_index = {'B': 0, 'G': 1, 'C': 2}
    
    # Asignar cada contenedor al color correspondiente
    for i in range(3):
        target_color = color_index[colors[i]]
        # Mover botellas que no corresponden al color deseado
        for j in range(3):
            if j != target_color:
                total_movements += bins[i][j]
    
    return total_movements

def main():
    input_lines = stdin.read().strip().split('\n')
    
    # Definir todas las permutaciones posibles de colores
    permutations = [
        'BGC',
        'BCG',
        'GBC',
        'GCB',
        'CBG',
        'CGB'
    ]
    
    for line in input_lines:
        numbers = list(map(int, line.split()))
        
        # Verificar que hay exactamente 9 números
        assert len(numbers) == 9
        
        # Dividir en grupos de tres números
        bins = [
            numbers[0:3],  # Botellas en el contenedor 1
            numbers[3:6],  # Botellas en el contenedor 2
            numbers[6:9]   # Botellas en el contenedor 3
        ]
        
        min_moves = float('inf')
        best_configuration = None
        
        # Evaluar cada permutación de colores
        for perm in permutations:
            moves = movement_calculaction(bins, perm)
            if moves < min_moves or (moves == min_moves and perm < best_configuration):
                min_moves = moves
                best_configuration = perm
        
        # Imprimir el resultado para la línea actual
        print(f"{best_configuration} {min_moves}")

main()
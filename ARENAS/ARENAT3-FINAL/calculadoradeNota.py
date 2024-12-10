def calcular_puntos(tipo, factor):
    return int(input(f"Ingrese los puntos {tipo} que obtuvo: ")) * factor

def imprimir_tabla(puntos, total, nota):
    print("\n+-----------------+---------------+")
    print("| Tipo de punto   | Puntos totales|")
    print("+-----------------+---------------+")
    for tipo, valor in puntos.items():
        print("| {:<15} | {:>13} |".format(tipo, valor))
    print("+-----------------+---------------+")
    print("| Total           | {:>13} |".format(total))
    print("+-----------------+---------------+")
    print("\nLa nota final es: {:.2f}".format(nota))

def main():
    k = 42
    puntos = {
        "Puntos de 1": calcular_puntos(1, 1),
        "Puntos de 2": calcular_puntos(2, 2),
        "Puntos de 3": calcular_puntos(3, 3),
        "Puntos de 4": calcular_puntos(4, 4),
    }
    
    total = sum(puntos.values())
    nota = 5 * (total / k)
    imprimir_tabla(puntos, total, nota)

main()

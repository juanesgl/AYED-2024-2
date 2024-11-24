from collections import deque
from sys import stdin

def process_deck(n):
    # Inicializar la cola con cartas del 1 al n
    deck = deque(range(1, n + 1))
    discarded = []

    while len(deck) > 1:
        # Descartar la carta en la parte superior
        discarded.append(deck.popleft())
        # Mover la nueva carta superior a la parte inferior
        deck.append(deck.popleft())

    # La carta restante
    remaining = deck.popleft()

    return discarded, remaining

def main():
    # Leer desde stdin
    for line in stdin:
        n = int(line.strip())
        if n == 0:
            break

        discarded, remaining = process_deck(n)

        # Formatear la salida
        if discarded:
            print(f"Discarded cards: {', '.join(map(str, discarded))}")
        else:
            print("Discarded cards: ")
        print(f"Remaining card: {remaining}")

main()
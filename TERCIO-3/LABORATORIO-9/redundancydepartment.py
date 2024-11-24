from sys import stdin

def read_input():
    return map(int, stdin.read().split())

def count_occurrences(sequence):

    occurrences = {}
    order = []
    for number in sequence:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
            order.append(number)
    return occurrences, order

def print_occurrences(occurrences, order):
  
    for number in order:
        print(f"{number} {occurrences[number]}")

def main():
    sequence = read_input()
    occurrences, order = count_occurrences(sequence)
    print_occurrences(occurrences, order)

main()
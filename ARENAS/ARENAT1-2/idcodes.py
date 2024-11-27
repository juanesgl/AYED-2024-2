from sys import stdin 
#ID Codes
""" We need to find the next permutation on the sequence based on the patron gived on the input, of the successor reach the end of the sequence we print No Successor"""

def next_permutation(sequence):
    sequence = list(sequence)  
    length = len(sequence)

    
    pivot_index = length - 2
    while pivot_index >= 0 and sequence[pivot_index] >= sequence[pivot_index + 1]:
        pivot_index -= 1

    if pivot_index == -1:
        return False  

    successor_index = length - 1
    while sequence[successor_index] <= sequence[pivot_index]:
        successor_index -= 1

    sequence[pivot_index], sequence[successor_index] = sequence[successor_index], sequence[pivot_index]

    sequence = sequence[:pivot_index + 1] + sequence[pivot_index + 1:][::-1]
    
    return ''.join(sequence)

def main():
    while True:
        line = stdin.readline().strip()

        if line == "#":
            break 

        result = next_permutation(line)

        if result:
            print(result)
        else:
            print("No Successor")

main()


from sys import stdin as wiggi

def main():

    entry  = int(wiggi.readline())

    sequence = ""
    count = 1

    while (len(sequence) < entry):
        entry -= len(sequence)
        sequence += [count] * str(count)
        count += 1
    print(sequence[entry - 1])
main()
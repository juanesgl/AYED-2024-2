from sys import stdin

def main():
    test_cases = int(stdin.readline().strip())  # Read the number of test cases
    for i in range(test_cases):
        # Read the input line, strip it, and split it into width and height
        inputs = stdin.readline().strip().split()
        width = int(inputs[0])
        height = int(inputs[1])
        # Calculate and print the number of 3x3 squares
        print((width // 3) * (height // 3))

main()
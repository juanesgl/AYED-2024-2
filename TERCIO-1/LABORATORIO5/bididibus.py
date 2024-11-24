from sys import stdin as dab

def bididibus(everything):
    water = 0
    stack = []

    for peperroni in range(len(everything)):
        symbol = everything[peperroni]
        if symbol == '\\':
            stack.append(peperroni)
        elif symbol == '/' and stack:
            start = stack.pop()
            water += peperroni - start
            
    return water

def main():
    test_cases = int(dab.readline().strip())
    
    results = []
    for watever in range(test_cases):
        everything = dab.readline().strip()
        results.append(bididibus(everything))

    for result in results:
        print(result)

main()
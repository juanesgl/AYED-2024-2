from sys import stdin

def main():
    cases = int(stdin.readline().strip())
    for x in range(cases):
        data = list(map(int, stdin.readline().strip().split()))
        number_of_relatives = data[0]
        street_numbers = data[1:]
        street_numbers.sort()
        median = street_numbers[number_of_relatives // 2]
        total_distance = sum(abs(median - street) for street in street_numbers)
        print(total_distance)
main()
from sys import stdin
def main():
    number_of_cases = int(stdin.readline().strip())
    stdin.readline()

    for _ in range(number_of_cases):
        if _ > 0:
            stdin.readline()
        number_of_people = int(stdin.readline().strip())
        crossing_times = []
        
        for _ in range(number_of_people):
            crossing_times.append(int(stdin.readline().strip()))
        print(crossing_times)

        if _ < number_of_cases -1:
            stdin.readline()

main()
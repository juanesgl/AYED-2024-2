from sys import stdin 


def main():
    test_cases = int(stdin.readline().strip())

    for _ in range(test_cases):

        town_citizens, pairs_of_people = map(int, stdin.readline().strip().split())


        disSet = [-1] * town_citizens

        for _ in range(pairs_of_people):
            citizen1, citizen2 = map(int, stdin.readline().strip().split())

            citizen1 -= 1
            citizen2 -= 1


            while disSet[citizen1] >= 0:
                citizen1 = disSet[citizen1]
            
            while disSet[citizen2] >= 0:
                citizen2 = disSet[citizen2]

            if citizen1 == citizen2:
                continue

            if citizen1 > citizen2:
                citizen1, citizen2 = citizen2, citizen1
            disSet[citizen1] += disSet[citizen2]
            disSet[citizen2] = citizen1

        print(-min(disSet))

if __name__ == "__main__":
    main()
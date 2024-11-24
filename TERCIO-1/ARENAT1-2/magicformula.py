from sys import stdin as formulin 


def contador_divisores(x_1, x_2, x_3, x_4, limit):
    count = 0
    for i in range(limit + 1):
        if (x_1 * i * i + x_2 * i + x_3) % x_4 == 0:
            count += 1
    return count


def main():
    x_1, x_2, x_3, x_4, limit = map(int, formulin.readline().split())

    while not (x_1 == 0 and x_2 == 0 and x_3 == 0 and x_4 == 0 and limit == 0):
        print(contador_divisores(x_1, x_2, x_3, x_4, limit))
        x_1, x_2, x_3, x_4, limit = map(int, formulin.readline().split())

main()
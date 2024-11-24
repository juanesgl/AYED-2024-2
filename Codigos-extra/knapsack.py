
def knapsack(P:list[int], B: list[int], m: int, i: int) -> int:
    if m <= 0 or i < 0:
        return 0

    if m < P[i]:
        return knapsack(P, B, m, i-1)

    a = knapsack(P, B, m - P[i], i-1) + B[i]
    b = knapsack(P, B, m, i-1)

    return max(a, b)

def knapsack2(P:list[int], B: list[int], m: int, i: int) -> tuple[int, list[int]]:
    if m <= 0 or i < 0:
        return 0, []

    if m < P[i]:
        return knapsack2(P, B, m, i-1)

    a, ca = knapsack2(P, B, m - P[i], i-1)
    a += B[i]
    ca += [P[i]]
    b, cb = knapsack2(P, B, m, i-1)

    if a > b:
        return (a, ca)
    else:
        return (b, cb)


def main():
    P = [12, 2, 1, 1, 4]  # pesos
    B = [ 4, 2, 1, 1, 10] # beneficios
    m = 15

    print(knapsack(P, B, m, len(P)-1))
    print(knapsack2(P, B, m, len(P)-1))

main()

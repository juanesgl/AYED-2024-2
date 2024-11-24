def knap(M, P:list[int], B: list[int], m: int, i: int) -> int:
    if M[m][i] is not None:
        return M[m][i]

    if m <= 0 or i < 0:
        return 0

    if m < P[i]:
        v = knap(M, P, B, m, i-1)
        M[m][i] = v
        return v

    a = knap(M, P, B, m - P[i], i-1) + B[i]
    b = knap(M, P, B, m, i-1)

    v = max(a, b)
    M[m][i] = v
    return v

def printm(M):
    for row in M:
        print(" ".join(map(str, row)))

def main():
    P = [12, 2, 1, 1, 4]  # pesos
    B = [ 4, 2, 1, 1, 10] # beneficios
    m = 15
    M = [[None for _ in range(len(P))] for _ in range(m+1)]
    assert len(M) == m + 1
    assert len(M[0]) == len(P)

    printm(M)
    print(knap(M, P, B, m, len(P)-1))
    printm(M)

main()

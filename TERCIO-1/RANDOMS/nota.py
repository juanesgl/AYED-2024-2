def grade(K, N) -> float:
    assert len(K) == 3
    assert len(K) == len(N)
    ka, kb, kc = K
    na, nb, nc = N
    n = 5.0 * min(1.0, (min(ka, na) + nb) / (ka + kb))
    n += min(1.0, nc / kc)

    return n


def main():
    line = input("Ka Kb Kb: ")
    ka, kb, kc = [int(i) for i in line.strip().split()]
    target = float(input("Target grade: "))
    assert 0.0 <= target <= 6.0

    print("Ka: %d | Kb: %d | Kc: %d" % (ka, kb, kc))
    table = []
    for na in range(0, ka + 1, 2):
        for nb in range(0, kb + ka + 1, 4):
            for nc in range(0, kc + 1, 5):
                if target < 5.0:
                    nc = 0
                notes = [na, nb, nc]
                n = grade([ka, kb, kc], notes)
                if -0.1 < n - target < 1.0:
                    table.append(notes + [n])
                    if target < 5.0:
                        break

    table.sort(key=lambda x: x[::-1])

    print("| na | nb | nc | Grade |")
    print("|----------------------|")
    for row in table:
        print("| {:2} | {:2} | {:2} | {:5.1f} |".format(*row))


if __name__ == "__main__":
    main()
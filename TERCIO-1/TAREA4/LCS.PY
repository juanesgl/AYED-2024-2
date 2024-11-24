def lcs_dynamic(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    lcs = []
    i, j = n, m
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return list(reversed(lcs)), dp[n][m]


X = [1, 0, 0, 1, 0, 1, 0, 1]
Y = [1, 0, 0, 1, 0, 1, 0, 1]

lcs, length = lcs_dynamic(X, Y)
print("LCS:", lcs)
print("Longitud del LCS:", length)
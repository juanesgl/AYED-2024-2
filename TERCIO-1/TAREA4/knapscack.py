import timeit

# Función de la mochila sin memorización (recursiva)
def knapsack_recursive(m, i, p, b):
    if m <= 0 or i <= 0:
        return 0
    elif m >= p[i-1]:
        return max(knapsack_recursive(m - p[i-1], i - 1, p, b) + b[i-1],
                   knapsack_recursive(m, i - 1, p, b))
    else:
        return knapsack_recursive(m, i - 1, p, b)

# Función de la mochila con memorización
def knapsack_memo(m, i, p, b, memo):
    if m <= 0 or i <= 0:
        return 0
    if memo[m][i] != -1:
        return memo[m][i]
    if m >= p[i-1]:
        memo[m][i] = max(knapsack_memo(m - p[i-1], i - 1, p, b, memo) + b[i-1],
                         knapsack_memo(m, i - 1, p, b, memo))
    else:
        memo[m][i] = knapsack_memo(m, i - 1, p, b, memo)
    return memo[m][i]

# Datos del problema
M = 50  
p = [10, 20, 30]  
b = [60, 100, 120]  
n = len(p)

# Medir tiempo para la función recursiva sin memorización
def test_recursive():
    knapsack_recursive(M, n, p, b)

# Medir tiempo para la función con memorización
def test_memo():
    memo = [[-1] * (n + 1) for _ in range(M + 1)]
    knapsack_memo(M, n, p, b, memo)

# Usar timeit para medir el tiempo de ejecución
time_recursive = timeit.timeit("test_recursive()", globals=globals(), number=1000)
time_memo = timeit.timeit("test_memo()", globals=globals(), number=1000)

print("Tiempo promedio (sin memorización) para 1000 ejecuciones: {:.6f} segundos".format(time_recursive))
print("Tiempo promedio (con memorización) para 1000 ejecuciones: {:.6f} segundos".format(time_memo))

def knapsack_tabulacion(M, p, b):
    n = len(p)
    dp = [[0 for pepperoni in range(M + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for m in range(1, M + 1):
            if m >= p[i-1]:
                dp[i][m] = max(dp[i-1][m], dp[i-1][m - p[i-1]] + b[i-1])
            else:
                dp[i][m] = dp[i-1][m]
    
    return dp[n][M]


resultado = knapsack_tabulacion(M, p, b)
print("Valor máximo (con tabulación):", resultado)



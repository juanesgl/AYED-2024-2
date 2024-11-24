import math

def memoized_cut_rod_aux(prices, n, revenue, cuts):
    if revenue[n] >= 0:
        return revenue[n]
    
    if n == 0:
        max_revenue = 0
    else:
        max_revenue = -math.inf
        for i in range(1, n + 1):
            current_revenue = prices[i - 1] + memoized_cut_rod_aux(prices, n - i, revenue, cuts)
            if current_revenue > max_revenue:
                max_revenue = current_revenue
                cuts[n] = i  

    revenue[n] = max_revenue
    return max_revenue

def memoized_cut_rod(prices, n):
    revenue = [-math.inf] * (n + 1)
    cuts = [0] * (n + 1)
    max_revenue = memoized_cut_rod_aux(prices, n, revenue, cuts)
    
    solution = []
    while n > 0:
        solution.append(cuts[n])
        n -= cuts[n]

    return max_revenue, solution


prices = [1, 5, 8, 9, 10, 17, 17, 20]  
n = 8  

max_revenue, solution = memoized_cut_rod(prices, n)
print("Valor máximo obtenido:", max_revenue)
print("Longitudes óptimas para cortar la varilla:", solution)




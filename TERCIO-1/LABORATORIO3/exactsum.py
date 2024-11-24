
from sys import stdin

def binary_search(A, k):
  # implemente
  low, high = 0, len(A) - 1
  while low < high: 
    mid = (low + high) // 2
    if A[mid] == k:
      return mid
    if A[mid] < k:
      low = mid + 1
    else:
      high = mid
  return -1

"""
def solve_n2(prices: list[int], money: int) -> tuple[int, int]:
  # implemente
  n = len(prices)
  diff = abs(prices[0] - prices[-1])
  b1, b2 = prices[0],  prices[-1]
  for i in range(n):
    for j in range(i, n): 
      if (prices[i] + prices[j]) == money and diff > abs(prices[i] - prices[j]):
        diff = abs(prices[i] - prices[j])
        b1, b2 = prices[i],  prices[j]
  
  if b1 <= b2:
    return b1, b2
  else:
    return b2, b1
"""
def solve(prices: list[int], money: int) -> tuple[int, int]:
    # Ordenar la lista de precios
    prices.sort()
    i, j = 0, len(prices) - 1
    best_i, best_j = 0, 0
    
    while i < j:
        current_sum = prices[i] + prices[j]
        
        if current_sum == money:
            # Si la suma es igual al dinero, actualizar los mejores candidatos
            best_i, best_j = prices[i], prices[j]
            i += 1
            j -= 1
        elif current_sum < money:
            i += 1
        else:
            j -= 1

    return best_i, best_j

def main():
  
  line = stdin.readline().strip()
  while len(line) != 0:
    n = int(line)  # number of books
    prices = [int(i) for i in stdin.readline().split()]  # book prices
    m = int(stdin.readline().strip())  # money peter has
    #stdin.readline()  # empty line read
    assert n == len(prices)
    i, j = solve(prices, m)
    assert i + j == m, "i: %d, j: %d" % (i, j)
    assert i <= j
    print("Peter should buy books whose prices are %d and %d.\n" % (i, j))

    line = stdin.readline().strip()

main()
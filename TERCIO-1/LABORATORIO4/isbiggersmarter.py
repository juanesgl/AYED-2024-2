from sys import stdin

def dp(u, elephants, memo):
    if memo[u] != -1:
        return memo[u]
    
    ret = 1
    for i in range(u + 1, len(elephants)):
        if elephants[i][0] > elephants[u][0] and elephants[i][1] < elephants[u][1]:
            ret = max(ret, 1 + dp(i, elephants, memo))
    
    memo[u] = ret
    return ret

def imprimir_secuencia(u, length, elephants, memo):
    print(elephants[u][2])  
    for i in range(u + 1, len(elephants)):
        if memo[i] == length:
            imprimir_secuencia(i, length - 1, elephants, memo)
            return

def main():
    elephants = []  
    elephants_index = 1  

   
    for line in stdin:
        size, iq = map(int, line.strip().split())
        elephants.append((size, iq, elephants_index))  
        elephants_index += 1
    
    elephants.sort(key=lambda x: (x[0], -x[1]))
    
    memo = [-1] * len(elephants)
  
    max_length = 0
    for i in range(len(elephants)):
        max_length = max(max_length, dp(i, elephants, memo))
    
    print(max_length)

    for i in range(len(elephants)):
        if memo[i] == max_length:
            imprimir_secuencia(i, max_length - 1, elephants, memo)
            break
main()

""" 
from sys import stdin

def comparar(elefante):
    # Devuelve una tupla: (peso, -IQ)
    return (elefante[0], -elefante[1])

def dp(u, elephants, memo):
    if memo[u] != -1:
        return memo[u]
    
    ret = 1
    for i in range(u + 1, len(elephants)):
        if elephants[i][0] > elephants[u][0] and elephants[i][1] < elephants[u][1]:
            ret = max(ret, 1 + dp(i, elephants, memo))
    
    memo[u] = ret
    return ret

def imprimir_secuencia(u, length, elephants, memo):
    print(elephants[u][2])  # Imprime el índice original del elefante
    for i in range(u + 1, len(elephants)):
        if memo[i] == length:
            imprimir_secuencia(i, length - 1, elephants, memo)
            return

def main():
    elephants = []  # Lista para almacenar los elefantes
    elephants_index = 1  # Para identificar el número de cada elefante

    for line in stdin:
        size, iq = map(int, line.strip().split())
        elephants.append((size, iq, elephants_index))  # Guardamos (peso, IQ, índice original)
        elephants_index += 1
    
    elephants.sort(key=comparar)
    
    memo = [-1] * len(elephants)

    max_length = 0
    for i in range(len(elephants)):
        max_length = max(max_length, dp(i, elephants, memo))

    print(max_length)

    for i in range(len(elephants)):
        if memo[i] == max_length:
            imprimir_secuencia(i, max_length - 1, elephants, memo)
            break

main()



"""
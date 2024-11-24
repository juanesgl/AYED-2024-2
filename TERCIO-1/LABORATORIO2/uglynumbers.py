def main():
    lista = []
    p  = 35
    for i in range(p):
        for j in range(p):
            for k in range(p):
                n = (2 ** i) * (3 ** j) * (5 ** k)
                lista.append(n)
    
    lista.sort()
    #print(A)
    #print(len(A))
    print("The 1500'th ugly number is {}.".format(lista[1499]))

main()
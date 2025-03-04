 
from sys import stdin
 
def solve(monto):
    l = len(monto)
    promedio = sum(monto) / l
    saldos = sorted(int((i - promedio) * 100) for i in monto)
    izquierda, derecha = 0, l - 1
    intercambio_minimo = 0
 
    while izquierda < derecha:
        ajuste = min(-saldos[izquierda], saldos[derecha])
        saldos[izquierda] += ajuste
        saldos[derecha] -= ajuste
        intercambio_minimo += ajuste
        if saldos[izquierda] == 0:
            izquierda += 1
        if saldos[derecha] == 0:
            derecha -= 1
 
    return f"${intercambio_minimo / 100:.2f}"
 
def main():
    linea = stdin.readline().strip()
    while linea != "0":
        n = int(linea)
        monto = [float(stdin.readline().strip()) for _ in range(n)]
        stdin.readline()
        print(solve(monto))
        linea = stdin.readline().strip()
 
main()
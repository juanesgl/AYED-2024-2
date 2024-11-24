from sys import stdin

def main():
    
    while True:
        line = int(stdin.readline().strip())
        if line == 0:
            break
        
        stations = []
        for _ in range(line):
            stations.append(int(stdin.readline().strip()))
        
        stations.sort()

        can_complete_journey = True
        
        # Verificar las distancias entre las estaciones durante el trayecto de ida
        for i in range(1, len(stations)):
            if stations[i] - stations[i-1] > 200:
                can_complete_journey = False
                break
        
        # Comprobar si es posible llegar al final del trayecto y regresar
        if can_complete_journey:
            if (1422 - stations[-1]) > 100:
                can_complete_journey = False
        
        # Revisar si el vehículo puede regresar al punto de inicio
        for i in range(len(stations) - 1, 0, -1):
            if stations[i] - stations[i-1] > 200:
                can_complete_journey = False
                break
        
        if can_complete_journey:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")

main()
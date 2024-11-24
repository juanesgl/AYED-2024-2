from sys import stdin 

def main():
    numbers_of_persons = int(stdin.readline().strip())

    names = []
    for i in range(numbers_of_persons):
        name = stdin.readline().strip()  
        names.append(name)
         
    if names == sorted(names):
        print("INCREASING")
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

main()
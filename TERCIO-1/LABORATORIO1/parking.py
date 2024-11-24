from sys import stdin 

def min_distance(lis):
    return (max(lis) - min(lis)) * 2

def main():

    line = stdin.readline().strip()
    n = int(line)

    for x in range(n):

        line = stdin.readline().strip()
        line = [int(x) for x in stdin.readline().strip().split()]
        print(min_distance(line))
       
main()
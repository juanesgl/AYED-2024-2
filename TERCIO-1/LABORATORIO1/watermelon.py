from sys import stdin
def main():
    line = stdin.readline().strip() 
    w = int(line)
    if w % 2 == 0 and w != 2:
        print("YES")
    else:
        print("NO")
main()
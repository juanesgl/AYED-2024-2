from sys import stdin

def mcarthy91(n):

    if n >= 101:
        return mcarthy91(mcarthy91(n + 11))
    else:
        return n-10

def main():
    while True:
        line = stdin.readline().strip()
        n = int(line)
        if n == 0:
            break
        print("f(" + str(n) + ") = " + str(mcarthy91(n)))

main()




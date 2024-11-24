from sys import stdin

def calc(arr: list[int]):

    h = arr[0]
    high, low = 0,0
    for height in arr[1:]:
        if height > h:
            high += 1
        elif height < h:
            low +=1
        h = height

    return(high,low)
def main():
    t = int(stdin.readline().strip())

    for i in range(t):
        n = int(stdin.readline().strip())
        nums = [int(i) for i in stdin.readline().strip().split()]

        a,b = calc(nums)
        print("Case {}: {} {}".format(i+1,a,b))
main()
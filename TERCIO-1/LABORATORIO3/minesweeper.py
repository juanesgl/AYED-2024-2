from sys import stdin

def read_input():
    fields = []
    field_number = 1
    while True:
        n, m = map(int, stdin.readline().strip().split())
        if n == 0 and m == 0:
            break
        field = [stdin.readline().strip() for _ in range(n)]
        fields.append((field_number, n, m, field))
        field_number += 1
    return fields

def process_field(n, m, field):
    result = [['0'] * m for _ in range(n)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                result[i][j] = '*'
            else:
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                        mine_count += 1
                result[i][j] = str(mine_count)
    
    return result

def main():
    fields = read_input()
    for field_number, n, m, field in fields:
        if field_number > 1:
            print()  # Print an empty line between fields
        print(f"Field #{field_number}:")
        result = process_field(n, m, field)
        for row in result:
            print(''.join(row))
main()

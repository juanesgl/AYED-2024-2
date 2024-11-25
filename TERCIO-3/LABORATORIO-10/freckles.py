import math
from sys import stdin

def calc_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_root(disjoint_set, x):
    if disjoint_set[x] != x:
        disjoint_set[x] = get_root(disjoint_set, disjoint_set[x])
    return disjoint_set[x]

def merge_sets(disjoint_set, heights, x, y):
    root_x = get_root(disjoint_set, x)
    root_y = get_root(disjoint_set, y)
    
    if root_x != root_y:
        if heights[root_x] > heights[root_y]:
            disjoint_set[root_y] = root_x
        elif heights[root_x] < heights[root_y]:
            disjoint_set[root_x] = root_y
        else:
            disjoint_set[root_y] = root_x
            heights[root_x] += 1

def solve_mst(total_points, coordinates):
    all_edges = [
        (calc_distance(coordinates[i], coordinates[j]), i, j)
        for i in range(total_points) 
        for j in range(i + 1, total_points)
    ]
    all_edges.sort()

    disjoint_set = list(range(total_points))
    heights = [0] * total_points

    total_ink = 0
    for ink_needed, vertex1, vertex2 in all_edges:
        if get_root(disjoint_set, vertex1) != get_root(disjoint_set, vertex2):
            merge_sets(disjoint_set, heights, vertex1, vertex2)
            total_ink += ink_needed
    return total_ink

def main():
    lines = stdin.read().strip().split("\n")
    cases = int(lines[0])
    curr_line = 1
    answers = []

    for _ in range(cases):
        if lines[curr_line] == "":
            curr_line += 1
        total_points = int(lines[curr_line])
        curr_line += 1
        coordinates = [tuple(map(float, lines[curr_line + i].split())) for i in range(total_points)]
        curr_line += total_points
        answers.append(f"{solve_mst(total_points, coordinates):.2f}")

    print("\n\n".join(answers))

if __name__ == "__main__":
    main()
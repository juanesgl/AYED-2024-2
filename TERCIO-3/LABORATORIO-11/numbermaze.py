from sys import stdin

def solve_maze_fast(maze, rows, cols):
    costs = [0] * cols
    costs[0] = maze[0][0]

   
    for j in range(1, cols):
        costs[j] = costs[j-1] + maze[0][j]

  
    for i in range(1, rows):
       
        costs[0] += maze[i][0]

        
        for j in range(1, cols):
            # Choose minimum path from left or top
            costs[j] = min(costs[j], costs[j-1]) + maze[i][j]
            
    return costs[-1]

def main():
    read = stdin.readline
    
    T = int(read())
    
    results = [0] * T
    
   
    for t in range(T):
       
        rows = int(read())
        cols = int(read())
        
        maze = [list(map(int, read().split())) for _ in range(rows)]
        
        results[t] = solve_maze_fast(maze, rows, cols)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
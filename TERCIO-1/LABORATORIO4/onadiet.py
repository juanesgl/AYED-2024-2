from sys import stdin

def main():
    test_cases = int(stdin.readline()) 
    for _ in range(test_cases):
        calorie_limit = int(stdin.readline())  
        num_food_items = int(stdin.readline())  
        calorie_values = []
        total_calories = 0
        dp = [False] * 501  

        
        food_calories = list(map(int, stdin.readline().split()))
        
        for calories in food_calories:
            calories //= 10  
            calorie_values.append(calories)
            total_calories += calories

        calorie_limit //= 10  

        if total_calories < calorie_limit:
            print("NO SOLUTION")
        else:
            dp[0] = True
            for i in range(num_food_items):
                for j in range(calorie_limit, -1, -1):
                    if dp[j]:
                        dp[j + calorie_values[i]] = True

            for i in range(calorie_limit, len(dp)):
                if dp[i]:
                    print(i * 10)
                    break
main()

from sys import stdin

def main():

    num_cases = int(stdin.readline().strip())
    
    for case_number in range(1, num_cases + 1):
        num_stations = int(stdin.readline().strip())
        current_sum = max_sum = start_index = end_index = temp_start = 0
        
        for station in range(1, num_stations):
            distance = int(stdin.readline().strip())
            current_sum += distance
            
            if current_sum < 0:
                current_sum = 0
                temp_start = station
            if current_sum > max_sum or (current_sum == max_sum and station - temp_start > end_index - start_index):
                max_sum = current_sum
                end_index = station
                start_index = temp_start
        
        if max_sum > 0:
            print(f"The nicest part of route {case_number} is between stops {start_index + 1} and {end_index + 1}")
        else:
            print(f"Route {case_number} has no nice parts")

main()

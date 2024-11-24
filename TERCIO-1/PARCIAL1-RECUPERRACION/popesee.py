from sys import stdin
from bisect import bisect_right

def popes(interval_years, num_popes, popes_list) :
    max_popes = 0
    start_year = 0
    end_year = 0
    
    for current_index in range(num_popes):
       
        upper_limit_index = bisect_right(popes_list, popes_list[current_index] + interval_years - 1)
        
        num_popes_in_range = upper_limit_index - current_index
        if num_popes_in_range > max_popes:
            max_popes = num_popes_in_range
            start_year = popes_list[current_index]
            end_year = popes_list[upper_limit_index - 1]
    
    return max_popes, start_year, end_year

def main():
    first_input = True
    
    for line in stdin:
        line = line.strip()
        
        if not line:
            continue
        
        if first_input:
            interval_years = int(line)
            first_input = False
        else:
            num_popes = int(line)
            popes_list = [int(next(stdin).strip()) for _ in range(num_popes)]
            max_popes, start_year, end_year = popes(interval_years, num_popes, popes_list)
            print(f"{max_popes} {start_year} {end_year}")
            first_input = True

main()
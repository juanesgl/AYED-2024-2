from sys import stdin
def zellers_congruence(day, month, year):
    # Adjust months and year for January and February
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    # Zeller's Congruence formula
    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

    # Convert Zeller's output to day of the week
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return days_of_week[h]

def main():
    input = stdin.read().strip()
    # Read the input lines
    lines = input.splitlines()
    
    for line in lines:
        if line:
            # Split the line into day, month, and year using basic string operations
            parts = line.split()
            day = int(parts[4])
            month = int(parts[1])
            year = int(parts[2])
            
            # Get the day of the week
            day_of_week = zellers_congruence(day, month, year)
            
            # Print the result
            print(f"{day:02d}/{month:02d}/{year} {day_of_week}")
main()
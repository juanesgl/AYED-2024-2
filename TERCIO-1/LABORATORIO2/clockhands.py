from sys import stdin

def calculate_angle(hour, minute):
 
    hour_angle = 30 * hour + (30 / 60) * minute
   
    minute_angle = 6 * minute

    angle = abs(hour_angle - minute_angle)
   
    smallest_angle = min(angle, 360 - angle)
    return smallest_angle

def main():
    for line in stdin:
        line = line.strip()  
        if line == '0:00':
            break  # Detiene la lectura si encuentra '0:00'
        hour, minute = map(int, line.split(':'))  
        angle = calculate_angle(hour, minute)  
        print(f"{angle:.3f}")  

main()
import sys
def main():
    input = sys.stdin.read().strip().splitlines()
    
    # Define the valid 5x3 digit representations
    digits_map = {
        ('***', '* *', '* *', '* *', '***'): '0',
        ('  *', '  *', '  *', '  *', '  *'): '1',
        ('***', '  *', '***', '*  ', '***'): '2',
        ('***', '  *', '***', '  *', '***'): '3',
        ('* *', '* *', '***', '  *', '  *'): '4',
        ('***', '*  ', '***', '  *', '***'): '5',
        ('***', '*  ', '***', '* *', '***'): '6',
        ('***', '  *', '  *', '  *', '  *'): '7',
        ('***', '* *', '***', '* *', '***'): '8',
        ('***', '* *', '***', '  *', '***'): '9',
    }
    
    # Extract digit blocks from input
    lines = input
    if not lines or len(lines) != 5:
        print("BOOM!!")
        return
    
    # Determine the number of digits
    num_digits = (len(lines[0]) + 1) // 4
    code = ""
    
    for i in range(num_digits):
        start_col = i * 4
        digit_block = tuple(line[start_col:start_col + 3] for line in lines)
        
        if digit_block in digits_map:
            code += digits_map[digit_block]
        else:
            print("BOOM!!")
            return
    
    # Convert the code to an integer
    code_number = int(code)
    
    # Check if the number is divisible by 6
    if code_number % 6 == 0:
        print("BEER!!")
    else:
        print("BOOM!!")

main()
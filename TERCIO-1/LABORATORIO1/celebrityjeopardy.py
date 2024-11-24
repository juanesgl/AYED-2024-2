from sys import stdin  # Import stdin from the sys module for reading input

def main():
    # Read all input from standard input (stdin) until EOF
    enter_information = stdin.read().strip()  
    
    # Split the input into individual lines
    lines = enter_information.splitlines()  
    
    # Iterate over each line
    for line in lines:  
        # Print each line
        print(line)  

# Call the main function to execute the code
main()
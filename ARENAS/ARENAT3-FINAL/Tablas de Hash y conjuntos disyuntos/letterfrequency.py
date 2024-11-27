from sys import stdin

def main():
    
    TC = stdin.readline().strip()

    for _ in range(int(TC)):
        letter_count = {}
        max_frequency = 0

       
        enter_string = stdin.readline().strip()

       
        for character in enter_string:
            if character.isalpha():  
                lower_char = character.lower()  
                if lower_char in letter_count:
                    letter_count[lower_char] += 1
                else:
                    letter_count[lower_char] = 1

              
                if letter_count[lower_char] > max_frequency:
                    max_frequency = letter_count[lower_char]
        
        
        most_frequent_letters = sorted([char for char, freq in letter_count.items() if freq == max_frequency])

        
        print("".join(most_frequent_letters))

main()

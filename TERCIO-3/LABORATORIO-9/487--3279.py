from sys import stdin
from collections import defaultdict

def main():
  
    letter_to_digit = {
        'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 
        'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6', 'P': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9'
    }

  
    input_data = stdin.read().strip().splitlines()

    
    results = []
    index = 1
    for _ in range(int(input_data[0])):
        num_numbers = int(input_data[index + 1])
        index += 2
        counts = defaultdict(int)

       
        for i in range(num_numbers):
           
            phone_input = input_data[index + i].strip().upper()

        
            phone_digits = [
                letter_to_digit.get(c, c) for c in phone_input if c.isdigit() or c in letter_to_digit
            ]

            phone = ''.join(phone_digits)[:7]

            if len(phone) == 7:
                formatted_phone = f"{phone[:3]}-{phone[3:]}"
                counts[formatted_phone] += 1

        # Filtrar y ordenar duplicados
        duplicates = sorted((num, cnt) for num, cnt in counts.items() if cnt > 1)

        if duplicates:
            results.extend(f"{num} {cnt}" for num, cnt in duplicates)
        else:
            results.append("No duplicates.")
        
        index += num_numbers
        results.append("")  

    print("\n".join(results).strip())


if __name__ == "__main__":
    main()

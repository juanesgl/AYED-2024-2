from sys import stdin as coke

def bottle_counter(number_of_bottles):
    total_bottles = 0

    while number_of_bottles >= 3:
        new_bottles = number_of_bottles // 3
        total_bottles += new_bottles  
        number_of_bottles = new_bottles + (number_of_bottles % 3)  

    if number_of_bottles == 2:  
        total_bottles += 1

    return total_bottles

def main():
  
    number_of_bottles = int(coke.readline().strip())

    while number_of_bottles != 0:
    
        print(bottle_counter(number_of_bottles))
       
        number_of_bottles = int(coke.readline().strip())

main()

from sys import stdin

def main():
   
    translations = {}
    
    lines = stdin.read().splitlines()
    
   
    for line in lines:
        if line == '':
            break
        english, foreign = line.split()
        translations[foreign] = english

    message_start = lines.index('') + 1
    
    for word in lines[message_start:]:
        print(translations.get(word, 'eh'))

if __name__ == "__main__":
    main()
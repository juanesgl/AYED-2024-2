from math import log10

def entropy(lam, word_dict):
    total = 0
    for count in word_dict.values():
        total += count * (log10(lam) - log10(count))
    return total / lam

def clean_text(line, specials):
    line = line.lower()
    for char in specials:
        line = line.replace(char, "")
    return line

def process_text_input(text_input, specials):
    word_dict = {}
    total_words = 0
    
    for text_line in text_input:
        text_line = clean_text(text_line, specials)
        words = text_line.split()
        
        for word in words:
            total_words += 1
            word_dict[word] = word_dict.get(word, 0) + 1

    return total_words, word_dict

def handle_text_block(lines, specials):
    total_words, word_dict = process_text_input(lines, specials)
    ent = entropy(total_words, word_dict)
    emax = log10(total_words)
    rel_ent = min(ent / emax * 100, 100)
    return total_words, ent, int(rel_ent)

def main():
    specials = [".", ",", ":", ";", "!", "¡", "?", "¿", "\\", "\"", "(", ")"]

    for line in iter(input, "****END_OF_INPUT****"):
        text_input = []
        
        while line != "****END_OF_TEXT****":
            text_input.append(line)
            line = input()
        
       
        total_words, ent, rel_ent = handle_text_block(text_input, specials)
        print(f"{total_words} {ent:.1f} {rel_ent}")

if __name__ == "__main__":
    main()

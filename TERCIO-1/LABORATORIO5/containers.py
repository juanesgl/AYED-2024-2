from sys import stdin

def count_stacks(s):
    stacks = [[]]
    stacks[0].append(s[0])
    
    for i in range(1, len(s)):
        char = s[i]
        mn = float('inf')
        mni = -1
        
        for j in range(len(stacks)):
            if stacks[j][-1] >= char:
                distance = ord(stacks[j][-1]) - ord(char)
                if distance < mn:
                    mn = distance
                    mni = j
        
        if mni == -1:
            stacks.append([char])
        else:
            stacks[mni].append(char)

    return len(stacks)

def main():
    case_number = 0
    for line in stdin:
        s = line.strip()
        if s[0] == 'e':
            break
        case_number += 1
        stack_count = count_stacks(s)
        print(f"Case {case_number}: {stack_count}")

main()

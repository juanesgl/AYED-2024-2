from sys import stdin
#History Grading
def longest_common_subsequence(correct_sequence, student_sequence, n):
 
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if correct_sequence[i] == student_sequence[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][n]

def main():
    input_data = stdin.read().strip().split('\n')
    
    correct_sequence = [0] * 25
    student_sequence = [0] * 25
    is_inputting_sequence = False
    num_elements = 0
    
    for line in input_data:
        sequence = list(map(int, line.split()))
        sequence_length = len(sequence)
        
        if is_inputting_sequence:

            for i in range(1, num_elements + 1):
                correct_sequence[sequence[i - 1]] = i
            is_inputting_sequence = False

        elif sequence_length == 1:
            num_elements = sequence[0]
            is_inputting_sequence = True
        else:
            for i in range(1, num_elements + 1):
                student_sequence[sequence[i - 1]] = i
            print(longest_common_subsequence(correct_sequence, student_sequence, num_elements))

main()
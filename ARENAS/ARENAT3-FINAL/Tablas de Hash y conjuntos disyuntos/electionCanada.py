from sys import stdin

def read_input():
    
    return stdin.read().strip().splitlines()

def process_candidates(lines, start_index):
    
    number_of_candidates = int(lines[start_index])
    candidates = {}
    
    current_index = start_index + 1
    for _ in range(number_of_candidates):
        candidate_name = lines[current_index]
        party_name = lines[current_index + 1]
        candidates[candidate_name] = party_name
        current_index += 2

    return candidates, current_index

def process_votes(lines, start_index, candidates):
    
    vote_count = int(lines[start_index])
    votes = {}

    current_index = start_index + 1
    for _ in range(vote_count):
        vote = lines[current_index]
        if vote in candidates:
            votes[vote] = votes.get(vote, 0) + 1
        current_index += 1

    return votes, current_index

def determine_winner(votes, candidates):
   
    if not votes:
        return "tie"
    
    max_votes = max(votes.values())
    winners = [cand for cand, count in votes.items() if count == max_votes]

    if len(winners) > 1:
        return "tie"
    else:
        winner = winners[0]
        return candidates[winner] if candidates[winner] != "independent" else "independent"

def main():
   
    lines = read_input()
    test_cases = int(lines[0])
    current_index = 1

    results = []

    for _ in range(test_cases):
        if lines[current_index] == "":
            current_index += 1  

        candidates, current_index = process_candidates(lines, current_index)
        votes, current_index = process_votes(lines, current_index, candidates)
        result = determine_winner(votes, candidates)
        results.append(result)

    
    print("\n\n".join(results))

if __name__ == "__main__":
    main()
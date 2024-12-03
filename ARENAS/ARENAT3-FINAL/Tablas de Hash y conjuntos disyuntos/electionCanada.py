from sys import stdin

def main():
    
    test_cases = int(stdin.readline().strip())
    stdin.readline()  

    results = []

    for _ in range(test_cases):
        
        number_of_candidates = int(stdin.readline().strip())

        
        candidates = {}
        votes_count = {}

       
        for _ in range(number_of_candidates):
            candidate_name = stdin.readline().strip()
            party_name = stdin.readline().strip()
            candidates[candidate_name] = party_name
            votes_count[candidate_name] = 0

    
        m = int(stdin.readline().strip())

       
        for _ in range(m):
            vote = stdin.readline().strip()
            if vote in votes_count:
                votes_count[vote] += 1

       
        max_votes = max(votes_count.values(), default=0)
        winners = [name for name, votes in votes_count.items() if votes == max_votes]

        if len(winners) > 1:
            results.append("tie")
        else:
            winner = winners[0]
            results.append(candidates[winner])

       
        if _ < test_cases - 1:
            stdin.readline()
    
    print(*results, sep="\n\n")

if __name__ == "__main__":
    main()
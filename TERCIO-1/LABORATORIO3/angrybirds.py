def main():
    num_cases = int(input())
    
    while num_cases > 0:
        num_cases -= 1
        
        num_producers, num_consumers = map(int, input().split())
        producer_prices = list(map(int, input().split()))
        consumer_prices = list(map(int, input().split()))
        
        combined_prices = producer_prices + consumer_prices
        combined_prices.append(0)
        
        producer_prices.sort()
        consumer_prices.sort()
        combined_prices.sort()
        
        optimal_price = 0
        min_angry_people = float('inf')
        producer_index, consumer_index = 0, 0
        
        for i in range(num_producers + num_consumers + 1):
            current_price = combined_prices[i]
            
            while producer_index < num_producers and producer_prices[producer_index] <= current_price:
                producer_index += 1
            
            while consumer_index < num_consumers and consumer_prices[consumer_index] < current_price:
                consumer_index += 1
            
            angry_count = num_producers - producer_index + consumer_index
            
            if angry_count < min_angry_people:
                min_angry_people = angry_count
                optimal_price = current_price
        
        print(optimal_price, min_angry_people)

if __name__ == "__main__":
    main()


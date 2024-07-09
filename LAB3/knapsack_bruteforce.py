from generatesubsets import generate_subsets

def knapsack_01_bruteforce(weights, profits, capacity):
    n = len(profits)
    max_profit = 0
    best_combination = []
    if capacity <= 0:
        return max_profit, best_combination
    subsets = [[]]
    for i in range(n):
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)
    for subset in subsets:
        total_weight = 0
        total_profit = 0
        for i in subset:
            total_weight += weights[i]
            total_profit += profits[i]
        if total_weight <= capacity and total_profit > max_profit:
            max_profit = total_profit
            best_combination = subset[:]
    return max_profit, best_combination

def knapsack_fractional_bruteforce(weights, profits, capacity):
    n = len(profits)
    max_profit = 0
    best_combination = []

    subsets = [[]]
    for i in range(n):
        new_subsets = [subset + [i] for subset in subsets]
        subsets.extend(new_subsets)
    
    if capacity <= 0:
        return max_profit, best_combination
    
    for subset in subsets:
        total_weight = 0
        total_profit = 0
        combination = []
        
        for i in subset:
            total_weight += weights[i]
            total_profit += profits[i]
            combination.append((i, 1))  # Fully included
        
        if total_weight <= capacity and total_profit > max_profit:
            max_profit = total_profit
            best_combination = combination[:]
        
        if total_weight > capacity:
            remaining_capacity = capacity
            total_profit = 0
            combination = []
            
            for item_index in subset:
                if weights[item_index] <= remaining_capacity:
                    combination.append((item_index, 1))
                    remaining_capacity -= weights[item_index]
                    total_profit += profits[item_index]
                else:
                    fraction = remaining_capacity / weights[item_index]
                    combination.append((item_index, fraction))
                    total_profit += profits[item_index] * fraction
                    break
            
            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combination[:]
    
    return max_profit, best_combination




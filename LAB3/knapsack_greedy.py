def knapsack_fractional_greedy(weights, profits, capacity):
    n = len(weights) 
    value_per_weight = [(i,profits[i] / weights[i], weights[i], profits[i]) for i in range(n)] 
    if capacity <= 0:
        return 0, [] 
    value_per_weight.sort(key=lambda x: (x[0], x[1]), reverse=True)
    max_profit = 0
    selected_items = []

 
    for index,ratio, weight, profit,in value_per_weight:
        if weight <= capacity:
            max_profit += profit
            
            selected_items.append((index, 1))
            capacity -= weight
        else:
            fraction = capacity / weight
            max_profit += profit * fraction
            selected_items.append((index, fraction))
            break
    selected_items.reverse()
    return max_profit, selected_items



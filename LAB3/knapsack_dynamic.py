def knapsack_01_dynamic(weights, profits, capacity):
    if capacity <= 0:
        return 0, []

    n = len(weights)
    data_table = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                data_table[i][w] = max(data_table[i - 1][w], profits[i - 1] + data_table[i - 1][w - weights[i - 1]])
            else:
                data_table[i][w] = data_table[i - 1][w]
    
 
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if data_table[i][w] != data_table[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    selected_items.reverse()
    return data_table[n][capacity], selected_items


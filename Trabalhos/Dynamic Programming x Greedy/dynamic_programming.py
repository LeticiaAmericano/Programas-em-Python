def dynamic_programming(items):
    optimal_items = []
    capacity = items['Capacidade da Mochila']
    weights = [item['Peso'] for item in items['Itens'].values()]

    for i in range(len(weights) + 1):
        row = []
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                row.append(0)
            elif weights[i - 1] <= j:
                row.append(max(optimal_items[i - 1][j - weights[i - 1]] + weights[i - 1], optimal_items[i - 1][j]))
            else:
                row.append(optimal_items[i - 1][j])
        optimal_items.append(row)

    i, j = len(weights), capacity
    selected_items = []
    while i > 0 and j > 0:
        if optimal_items[i][j] != optimal_items[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    selected_weights = [weights[item_idx] for item_idx in selected_items]
    selected_ids = [item_idx + 1 for item_idx in selected_items]  

    return sum(selected_weights), selected_ids
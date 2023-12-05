def greedy(items):
    total_weight = 0
    selected_items = []
    selected_ids = []

    capacity = items['Capacidade da Mochila']
    items_dict = items['Itens']
    sorted_items_list = sorted(items_dict.items(), key=lambda x: x[1]['Peso'])

    for item_id, item_details in sorted_items_list:
        if item_id not in selected_ids and total_weight + item_details['Peso'] <= capacity:
            total_weight += item_details['Peso']
            selected_items.append({'Item': item_id, 'Peso': item_details['Peso']})
            selected_ids.append(item_id)

    return selected_ids, total_weight
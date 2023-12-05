import random
import json
import os

def generate_input(num_inputs, max_capacity, max_items, max_weight):
    directory = "Dynamic Programming x Greedy"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, "inputs.txt"), 'w') as file:
        for i in range(num_inputs):
            capacity = random.randint(1, max_capacity)
            line_values = [str(capacity)]

            for j in range(max_items):
                item_weight = random.randint(1, max_weight)
                item_id = str(j + 1)
                line_values.extend([item_id, str(item_weight)])
            
            line = ",".join(line_values)
            file.write(f"{line}\n")

num_inputs = 100
max_capacity = 1000
max_items = 100
max_weight = 500

generate_input(num_inputs, max_capacity, max_items, max_weight)

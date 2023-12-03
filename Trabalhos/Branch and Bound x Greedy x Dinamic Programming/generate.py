import random

def generate_inputs(num_inputs):
    inputs = []
    for i in range(1, num_inputs + 1):
        # Gerando valores aleatórios para cada job
        id = i
        deadline = random.randint(1, 10)  # Altere o intervalo conforme necessário
        penalty = random.randint(20, 100)  # Altere o intervalo conforme necessário
        time = random.randint(1, 10)  # Altere o intervalo conforme necessário
        inputs.append(f"{id},{deadline},{penalty},{time}")
    return inputs

num_inputs = 10
inputs = generate_inputs(num_inputs)

# Escrever os inputs em um arquivo
with open("input.txt", "w") as file:
    for line in inputs:
        file.write(line + "\n")

import random

# Gera um conjunto de dados aleatório de tamanho 'size' no formato desejado
def generate_random_sequence(size):
    return ' '.join(str(random.randint(1, 100)) for _ in range(size))

# Gera 100 conjuntos de dados aleatórios e salva em um arquivo 'input.txt'
def save_to_file():
    num_sets = 5000  # Define o número de conjuntos desejados
    with open('input.txt', 'w') as file:
        for _ in range(num_sets):
            size = random.randint(5, 1000)  # Tamanho aleatório entre 5 e 15
            sequence = generate_random_sequence(size)
            file.write(sequence + '\n')

# Gera e salva 100 conjuntos de dados aleatórios no formato desejado no arquivo 'input.txt'
save_to_file()

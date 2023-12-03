from kadane import *
from brute_force import *
from divide_and_conquer import *

import time
import psutil

def read_input_file(filename):
    with open(filename, 'r') as file:

        all_number_list = []

        for line in file:
            all_number_list.append(list(map(int, line.strip().split())))

    return all_number_list

def find_max_subsequence(all_number_list, method):
    all_max_subsequences = []

    for number_list in all_number_list:
        max_subsequence = method(number_list)
        all_max_subsequences.append(max_subsequence)

    return all_max_subsequences

# Criterio de desempate: Primeira sequência encontrada

def measure_performance(algorithm, all_number_list):
    start_time = time.time()  # Marca o tempo inicial

    all_max_subsequences = []
    for number_list in all_number_list:
        max_subsequence = algorithm(number_list)
        all_max_subsequences.append(max_subsequence)

    end_time = time.time()  # Marca o tempo final
    execution_time = end_time - start_time  # Calcula o tempo de execução

    # Utilize psutil para medir o uso de memória
    process = psutil.Process()
    memory_usage = process.memory_info().rss  # Mede o uso de memória em bytes

    return all_max_subsequences, execution_time, memory_usage

def iterate_and_print_results(algorithm_name, algorithm_function, all_number_list):
    all_max_subsequences, exec_time, mem_usage = measure_performance(algorithm_function, all_number_list)
    print_algorithm_results(algorithm_name, exec_time, mem_usage, all_max_subsequences)

def print_algorithm_results(algorithm_name, exec_time, mem_usage, all_max_subsequences):
    print(algorithm_name)
    print("-----------------------")
    print("Tempo de execução:", exec_time)
    print("Uso de memória:", mem_usage)
    # print_result_number_list(all_max_subsequences)
    print("-----------------------")

def print_result_number_list(all_max_subsequences):
    for result in all_max_subsequences:
        print("Maior subsequência crescente encontrada:", result)


if __name__ == "__main__":
    all_number_list = read_input_file('input.txt')

     # Utilizando o método de força bruta
    iterate_and_print_results("Força bruta", find_max_sequence_force_brute, all_number_list)

    # Utilizando o algoritmo de Kadane
    iterate_and_print_results("Algoritmo de Kadane", find_max_sequence_Kadane, all_number_list)

    # Utilizando o algoritmo de Divisão e Conquista
    iterate_and_print_results("Algoritmo de Divisão e Conquista", longest_subsequence, all_number_list)
from dynamic_programming import *
from greedy import *
import psutil
import time
import os

def read_input():
    directory = "Dynamic Programming x Greedy"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, "inputs.txt"), 'r') as file:
        itens_list = []
        for line in file:
            values = line.strip().split(',')
            capacity = int(values[0])
            items = {}

            for i in range(1, len(values), 2):
                item_id = values[i]
                item_weight = int(values[i + 1])
                items[item_id] = {"Peso": item_weight}

            itens_list.append({"Capacidade da Mochila": capacity, "Itens": items})

    return itens_list

def main():
    itens_list = read_input()

    for i in range(1,3):
        if (i==1):

            print("Algortimo de Greedy")
            print("------------------------------------------------------------------------")

            start_time = time.time()  
            start_memory = psutil.Process().memory_info().rss  

            for i, items in enumerate(itens_list, start=1):
                capacity = items['Capacidade da Mochila']
                selected_items, total_weight = greedy(items)
                
                # print(f"Resultados para o input {i}:")
                # print("------------------------------------------------------------------------")
                # print(f"Itens selecionados: {selected_items}")
                # print("------------------------")
                # print(f"Capacidade da mochila: {capacity}")
                # print(f"Peso total: {total_weight}")
                # print("------------------------")

            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss 
            execution_time = end_time - start_time
            memory_used = end_memory - start_memory
            print("------------------------")
            print(f"Tempo de execução total: {execution_time} segundos")
            print(f"Memória utilizada total: {memory_used} bytes")
            print("------------------------")

        if (i==2):

            print("Algortimo de Programação Dinâmica")
            print("------------------------------------------------------------------------")

            start_time = time.time()  
            start_memory = psutil.Process().memory_info().rss  

            for i, items in enumerate(itens_list, start=1):
                capacity = items['Capacidade da Mochila']
                selected_weight, selected_ids = dynamic_programming(items)
                
                # print(f"Resultados para o input {i}:")
                # print("------------------------------------------------------------------------")
                # print(f"Itens selecionados: {selected_items}")
                # print("------------------------")
                # print(f"Capacidade da mochila: {capacity}")
                # print(f"Peso total: {selected_weight}")
                # print("------------------------")

            end_time = time.time()
            end_memory = psutil.Process().memory_info().rss 
            execution_time = end_time - start_time
            memory_used = end_memory - start_memory
            print("------------------------")
            print(f"Tempo de execução total: {execution_time} segundos")
            print(f"Memória utilizada total: {memory_used} bytes")
            print("------------------------")

main()
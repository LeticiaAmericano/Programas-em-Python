from greedy import * 
from branch_and_bound import *

class Job:
    def __init__(self, id, deadline, penalty, time):
        self.id = id
        self.deadline = deadline
        self.penalty = penalty
        self.time = time

def read_input():
    jobs = []
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        for i in lines:
            data = i.strip().split(',')
            id, deadline, penalty, time = map(int, data)
            trabalho = Job(id, deadline, penalty, time)
            jobs.append(trabalho)
    return jobs

def main():

    jobs = read_input()

    for i in range(1,3):
        if (i==1):
            
            sequence, total_penalty, total_time, memory_used = greedy(jobs)

            print("Greedy")
            print("------------------------")
            print("Sequência de trabalhos:", sequence)
            print("Penalidade total:", total_penalty)
            print("Tempo total:", total_time)
            print("Memoria utilizada:", memory_used)
            print("------------------------")
        if (i==2):
            start_time = time.time()
            best_sequence, best_penalty = branch_and_bound(jobs, [])
            end_time = time.time() 
            total_time = end_time - start_time
            print("Branch and Bounch")
            print("------------------------")
            print("Sequência de trabalhos:", [job.id for job in best_sequence])
            print("Penalidade total:", best_penalty)
            print("Tempo total:", total_time)

main()
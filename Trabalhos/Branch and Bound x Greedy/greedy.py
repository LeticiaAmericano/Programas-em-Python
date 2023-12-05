import resource
import time

def greedy(jobs):
    start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    start_time = time.time()  
    jobs.sort(key=lambda x: x.penalty, reverse=True) 
    current_time = 0
    total_penalty = 0
    sequence = []
    
    for job in jobs:
        current_time += job.time
        
        if current_time > job.deadline:
            penalty = current_time - job.deadline
            total_penalty += penalty
        sequence.append(job.id)
    
    end_time = time.time() 
    execution_time = end_time - start_time 
    end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    memory_used = end_memory - start_memory
    
    return sequence, total_penalty, execution_time, memory_used
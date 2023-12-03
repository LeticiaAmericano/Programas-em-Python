best_sequence = None
best_penalty = None

def calculate_penality(jobs): 
    current_time = 0
    total_penalty = 0

    for job in jobs:
        current_time += job.time
        
        if current_time > job.deadline:
            penalty = current_time - job.deadline
            total_penalty += penalty
    
    return total_penalty


def branch_and_bound(jobs, current_jobs):
    global best_sequence
    global best_penalty

    if len(jobs) == 0:
        best_sequence = current_jobs
        best_penalty = calculate_penality(current_jobs)
        return
    
    for job in jobs:
        jobs_without_current = [j for j in jobs if j != job]
        new_current_jobs = current_jobs + [job]     

        if best_penalty != None and best_penalty <= calculate_penality(new_current_jobs):
            return

        branch_and_bound(jobs_without_current, new_current_jobs)

    return best_sequence, best_penalty

    
        
    
      

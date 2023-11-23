def update_max_subsequence_Kadane(current_max, max_subsequence):
    if len(current_max) > len(max_subsequence):
        return list(current_max)
    else:
        return list(max_subsequence)

def find_max_sequence_Kadane(sequence):
    current_max = max_subsequence = [sequence[0]]  

    for i in range(1, len(sequence)):
        if sequence[i] > current_max[-1]:
            current_max.append(sequence[i])
        else:
            current_max = [sequence[i]]

        max_subsequence = update_max_subsequence_Kadane(current_max, max_subsequence)

    return max_subsequence


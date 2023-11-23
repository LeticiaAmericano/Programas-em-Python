def find_max_sequence_force_brute(sequence):
    max_length = 0
    max_subsequence = []

    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            subsequence = sequence[i:j+1]
    
            is_sequence = True

            for k in range(len(subsequence)-1):
                if subsequence[k] >= subsequence[k+1]:
                    is_sequence = False
                    break

            if is_sequence and len(subsequence) > max_length:
                max_length = len(subsequence)
                max_subsequence = subsequence

    return max_subsequence if max_length > 0 else sequence


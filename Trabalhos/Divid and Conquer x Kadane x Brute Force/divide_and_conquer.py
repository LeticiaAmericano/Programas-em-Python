def divide_increasing_subsequences(number_list):
    subsequences = []
    current_subsequence = [number_list[0]]

    for i in range(1, len(number_list)):
        if number_list[i] >= number_list[i - 1]:
            current_subsequence.append(number_list[i])
        else:
            subsequences.append(current_subsequence)
            current_subsequence = [number_list[i]]

    if current_subsequence:
        subsequences.append(current_subsequence)

    return subsequences

def longest_subsequence(number_list):

    subsequences = divide_increasing_subsequences(number_list)

    max_subsequence = max(subsequences, key=len)
    return max_subsequence


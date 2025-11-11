def solution(sequence):
    answer = 0
    sequence1 = []
    sequence2 = []

    pulse = 1
    for i in range(len(sequence)):
        pulse = 1 if i % 2 else -1
        sequence1.append(pulse * sequence[i])
        sequence2.append(-pulse * sequence[i])

    for i in range(1, len(sequence)):
        sequence1[i] = max(sequence1[i], sequence1[i - 1] + sequence1[i])
        sequence2[i] = max(sequence2[i], sequence2[i - 1] + sequence2[i])

    return max(max(sequence1), max(sequence2))

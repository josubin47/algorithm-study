from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()

    return list(Counter(participant) - Counter(completion))[0]
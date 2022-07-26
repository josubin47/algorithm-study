def solution(arr):
    answer = []
    for idx, val in enumerate(arr):
        if idx+1 == len(arr):
            answer.append(val)
            break
            
        if val != arr[idx+1]:
            answer.append(val)
    return answer
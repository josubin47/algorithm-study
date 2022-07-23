from itertools import permutations

def solution(numbers): 
    arr = list(numbers)
    permutationsArr = []
    cnt = 0
    
    for i in range(len(arr)):
        permutationsArr += list(map(int, map(''.join ,permutations(arr, i+1))))
        
    
    for v in set(permutationsArr):
        flag = True
        
        if v == 1 or v == 0:
            continue
            
        for i in range(2, v):
            if v % i == 0:
                flag = False
                break
                
        if flag == True:
            cnt += 1
            
    return cnt
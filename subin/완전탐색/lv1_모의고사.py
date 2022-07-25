def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for index, num in enumerate(answers):
        if num == one[index % len(one)]:
            score[0] += 1
        if num == two[index % len(two)]:
            score[1] += 1
        if num == three[index % len(three)]:
            score[2] += 1
    
    maxVal = max(score)
    
    for index, num in enumerate(score):
        if maxVal == num:
            answer.append(index + 1)
    
    return answer;

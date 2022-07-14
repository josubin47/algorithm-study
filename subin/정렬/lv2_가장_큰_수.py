from functools import cmp_to_key

def compare(a, b):
    return int(b + a) - int(a + b);

def solution(numbers):
    strList = list(map(str, numbers))
    numbers = sorted(strList, key=cmp_to_key(compare))

    if numbers[0] == '0':
        return '0';
    else:
        return''.join(str(i) for i in numbers)
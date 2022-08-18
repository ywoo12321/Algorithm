import sys
input = sys.stdin.readline
#fun
def put_in_operator(start,value):
    global max_num, min_num
    if start == n:
        max_num = max(max_num,value)
        min_num = min(min_num,value)
    else:
        if operators[0] > 0:
            operators[0] -= 1
            put_in_operator(start + 1, value + num_li[start])
            operators[0] += 1
        if operators[1] > 0:
            operators[1] -= 1
            put_in_operator(start + 1, value - num_li[start])
            operators[1] += 1
        if operators[2] > 0:
            operators[2] -= 1
            put_in_operator(start + 1, value * num_li[start])
            operators[2] += 1
        if operators[3] > 0:
            operators[3] -= 1
            put_in_operator(start + 1, int(value / num_li[start]))
            operators[3] += 1

#in
n = int(input().rstrip())
num_li = list(map(int, input().split()))
operators = list(map(int, input().split()))
#out
max_num = -1e9
min_num = 1e9
put_in_operator(1, num_li[0])
print(max_num)
print(min_num)

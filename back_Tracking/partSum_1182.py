import sys
input = sys.stdin.readline
#fun
def part_sum(num1, past_sum):
    global answer
    global cnt
    if num1 >= theNumberOfNum:
        return
    past_sum = past_sum + num_li[num1]
    if past_sum == answer:
        cnt += 1
    part_sum(num1 + 1, past_sum)
    past_sum -= num_li[num1]
    part_sum(num1 + 1, past_sum)

#in
theNumberOfNum, answer = map(int,input().split())
num_li = list(map(int,input().split()))
cnt = 0
#out
part_sum(0, 1)
print(cnt)
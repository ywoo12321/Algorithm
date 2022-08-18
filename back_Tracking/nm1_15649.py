import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
#fun
def dfs(max_num, line):
    global stack
    if len(stack) == line:
        print(*stack, sep = ' ')
    for i in range(1, max_num + 1):
        if i not in stack: # 겹치는 숫자 없을 때 숫자 집어 넣기
            stack.append(i)
            dfs(max_num, line)
            stack.pop()
        
#in
max_num, line = map(int, input().split())
#out
stack = []
dfs(max_num, line)
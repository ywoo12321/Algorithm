import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(max_num, line):
    global stack
    if len(stack) == line:
        print(*stack, sep = ' ')
        return
    for i in range(1, max_num + 1):
        stack.append(i)
        dfs(max_num, line)
        stack.pop()
    
#in
max_num, line = map(int,input().split())
#out
stack = []
dfs(max_num,line)


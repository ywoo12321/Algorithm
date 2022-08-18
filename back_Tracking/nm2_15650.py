import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start):
    global stack
    if len(stack) == line:
        print(*stack, sep = ' ')
        return
    for i in range(start, max_num + 1):
        if i not in stack:
            stack.append(i)
            dfs(i)
            stack.pop()
        
    
#in
max_num, line = map(int,input().split())
#out
stack = []
dfs(1)


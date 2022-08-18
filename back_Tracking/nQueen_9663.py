import sys
input = sys.stdin.readline

#fun
def nQueen(start):
    global queen_cnt
    global row
    if start == n:
        queen_cnt += 1
    else:
        for i in range(0, n):
            row[start] = i
            if isQueen(start) == True:
                nQueen(start + 1)
            row[start] = 0
def isQueen (col): #queen 대각선 좌우 위아래 공격 못함
    for i in range(col):
        if row[col] == row[i] or abs(row[col] - row[i]) == abs(col - i):
            return False
    return True
#in
n = int(input().rstrip())
#out
queen_cnt = 0
row = [0] * n
nQueen(0)
print (queen_cnt)
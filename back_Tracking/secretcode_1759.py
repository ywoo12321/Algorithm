import sys
from itertools import combinations 
input = sys.stdin.readline
#fun
def can_password(alphabet, password_length):
    password = combinations(alphabet,password_length)
    password = list(password)
    password.sort()
    
    jaeum_cnt = 0
    moeum_cnt = 0
    for i in range(len(password)):
        for word in password[i]:
            if word 
        if #aeiou 2개 이상, 자음 1개 이상 일때:
            print(''.join(password[i]))
    
#in
password_length, the_num_of_alphabet = map(int, input().split())
alphabet = list(map(str, input().split()))
#out
can_password(password_length, alphabet)

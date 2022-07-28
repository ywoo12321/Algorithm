

# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 둘째 줄에 세준이의 현재 성적이 주어진다. 
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 출력

# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
import sys
input = sys.stdin.readline
#fun
def new_avg():
    # global score_each, num_object
    max_score = max(score_each)
    new_score = []
    for score in score_each:
        new_score.append((score/max_score) * 100)
    answer = sum(new_score) / num_object
    return answer
#in
num_object = int(input().rstrip())
score_each = list(map(int, input().split()))
#out
print(new_avg())
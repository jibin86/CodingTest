# 성적이 낮은 순서로 학생 출력하기

# 쌍으로 움직여야하면 튜플을 사용하기!

# 학생 수 입력 받기
n = int(input())

# 학생 이름, 성적 입력 받기
score = []
for i in range(n):
    input_data = input().split()
    score.append((input_data[0], int(input_data[1])))
    
# 성적이 낮은 순서대로 학생 이름 출력
score = sorted(score, key=lambda pick: pick[1])

# 정렬된 이름 출력
for i in score:
    print(i[0], end=' ')

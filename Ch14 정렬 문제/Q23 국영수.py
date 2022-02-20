# 백준 10825번
# 국영수

#학생 수 입력 받기
n = int(input())

# 한 줄에 하나씩 학생의 이름, 국어, 영어, 수학 점수를 튜플로 입력 받기
students = []
for student in range(n):
    input_data = list(input().split())
    students.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))

# 이름 사전순 증가 순으로 정렬
students = sorted(students, key=lambda array: array[0], reverse=False)
# 수학 점수 감소 순
students = sorted(students, key=lambda array: array[3], reverse=True)
# 영어 점수 증가 순
students = sorted(students, key=lambda array: array[2], reverse=False)
# 국어 점수 감소 순
students = sorted(students, key=lambda array: array[1], reverse=True)

for student in students:
    print(student[0])

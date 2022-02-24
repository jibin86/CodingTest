#상하좌우
#한번에 변수 정의하기 : x, y = 1, 1
#for문에서 어떤 조건일 때 시행 건너 뛰기 :  continue

n = int(input())
plans = input().split()

x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    #이동 수행
    x, y = nx, ny

print(x, y)

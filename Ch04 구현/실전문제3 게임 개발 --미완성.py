# 게임 개발

print(-1 % 4)

n, m = map(int, input().split())
x, y, way = map(int, input().split())
map = []

# 방향이 북 동 남 서일 때
move_types = [(0, -1), (-1, 0), (0, 1), (1, 0)]
---> 지우고 + - 로 바꾸기

#가본 곳을 3으로 표시

#맵 생성
for i in range(n):
    map.append(list(map(int, input().split())))

count = 0
while True:
    #사방이 막혀있는지 확인
    if map[x+1][y] != 0 or map[x][y+1] != 0 or map[x-1][y] != 0 or map[x][y-1] != 0 :
        
        
    #회전
    way = (way - 1) % 4

    #다음 스텝
    nx = x + move_types[way][0]
    ny = y + move_types[way][1]
    if map[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        map[nx][ny] = 3
    elif map[nx][ny] == 1 or map[nx][ny] == 3:
        continue

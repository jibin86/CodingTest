# 게임 개발

# 맵 크기
n, m = map(int, input().split())

# 게임 캐릭터가 있는 칸의 좌표와, 바라보는 방향 d를 입력 받기
# 북:0, 동:1, 남:2, 거:3 -> 시계방향
x, y, d = map(int, input().split())

# 맵 입력 받기
# 육지:0, 바다:1
graph = [list(map(int,input().split())) for _ in range(n)]

# d에 따른 캐릭터의 정면 방향 위치
# 북 동 남 서 방향
move = ((-1,0), (0,1), (1,0), (0,-1))

def move_check(x, y):
    if graph[x][y-1] == 0 or graph[x][y+1] == 0 or graph[x+1][y] == 0 or graph[x+1][y] == 0:
        return True
    else:
        return False
    
count = 1

graph[x][y] = -1


while True:
    # 사방이 바다이거나 이미 가본 칸이면 뒤로 한 칸
    if not move_check(x,y):
        nx = x - move[d][0]
        ny = y - move[d][1]
        # 뒤가 바다이면 종료
        if graph[nx][ny] == 1:
            break
        else:
            #뒤로 한 칸
            x = nx
            y = ny
            continue
            
    # 캐릭터의 왼쪽이 0이면 왼쪽으로 회전 후, 왼쪽으로 전진 (앞으로만 갈 수 있음)
    d = (d-1) % 4
    nx = x + move[d][0]
    ny = y + move[d][1]
    if graph[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        # 방문 기록
        graph[x][y] = -1
    # 캐릭터의 왼쪽이 0이 아니면 왼쪽으로 회전만

print(count)

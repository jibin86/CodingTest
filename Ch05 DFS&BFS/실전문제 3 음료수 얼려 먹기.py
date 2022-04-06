#음료수 얼려먹기

#DFS를 이용하여

# 얼음판 크기 입력받기
n, m = map(int, input().split())

# 얼음판 graph 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 얼음판 확인
print(graph)

# 상, 하, 좌, 우 방향 키
ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    # 그래프의 현재 좌표가 x < 0, x >= n, y < 0, y >= m 이거나 현재 위치가 1이면 함수 종료 시키기
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 1:
        return False
    # 방문 표시
    graph[x][y] = 1

    # 상하좌우 확인
    for i in range(4):
        nx = x + ways[i][0]
        ny = y + ways[i][1]

        dfs(nx, ny)
    return True

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1
print(count)






# N, M을 공백을 입력받기
n, m = map




    

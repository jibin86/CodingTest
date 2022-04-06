# 미로 탈출

from collections import deque

# 미로 크기 입력 받기
n, m = map(int, input().split())

# 미로 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    # 큐 선언
    queue = deque()
    # 현재 위치 삽입, 방문 처리
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        # 큐 꺼내고 꺼낸 걸로 시작!!!
        x, y = queue.popleft()
        #상, 하, 좌, 우 살피기
        for i in range(4):
            nx = x + ways[i][0]
            ny = y + ways[i][1]
            # nx, ny가 미로 밖을 벗어나면 pass
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 현재 좌표에 괴물이 없으면(1이면) 인접 노드 삽입 후 방문 처리하기
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return
bfs(0, 0)
print(graph[n-1][m-1])
    

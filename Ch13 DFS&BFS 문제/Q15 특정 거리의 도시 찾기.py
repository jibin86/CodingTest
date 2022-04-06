from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호 입력받기
n, m, k, x = map(int, input().split())

# 도로 입력 받기
# 그래프 초기화하기
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
queue = deque()
queue.append(x)
visited[x] = 0

while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
if k not in visited:
    print(-1)
else:
    for i in range(1,n+1):
        if visited[i] == k:
            print(i)

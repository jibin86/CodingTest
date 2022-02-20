# 백준 18352번

# 리스트 원소 제거 : del a[a.index('찾을 아이템')]
#                  : a.remove('찾을 아이템') --> 찾을 아이템이 없으면 ValueError 발생

# 특정 거리의 도시 찾기
from collections import deque

# n, m, k, x 입력 받기
n, m, k , x = map(int, input().split())

# 도로 입력 받기 (인접 리스트)
road = [[] for _ in range(m+1)]
for i in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    
visited = [False] * (n + 1)
count = [0] * (n + 1)
result = []

def bfs(x):
    # x는 현재 도시 번호, 현재 위치 삽입
    queue = deque([x])
    # 방문 표시
    visited[x] = 0
    while queue:
        # 꺼내고 현재 위치로 설정
        now = queue.popleft()
        for i in road[now]:
            # 방문 안 한 노드이면
            if not visited[i]:
                # 인접 노드 삽입
                queue.append(i)
                # 방문 처리
                visited[i] = visited[now] + 1 
                if visited[i] == k:
                    result.append(i)
if k == 0:
    print(x)
else:
    bfs(x)
    if result:
        for i in result:
            print(i)       
    else:
        print(-1)

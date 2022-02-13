# DFS 메서드 정의

# dfs(그래프 리스트, 노드 번호, 방문 여부 리스트)
# visited의 인덱스 번호는 노드 번호를 의미
def dfs(graph, start, visited):
    #현재 노드를 방문처리 True
    visited[start] = True
    print(start, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)




# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9   # 0 ~ 8

dfs(graph, 1, visited)

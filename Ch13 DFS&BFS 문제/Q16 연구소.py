## 조합 from itertools import combinations
##      list(combinations(items, 2))

from itertools import combinations

def dfs(x, y):
    # 상, 하, 좌, 우로 움직이기
    for way in ways:
        nx = x + way[0]
        ny = y + way[1]
        # 지도를 벗어나거나 벽이면 false 리턴
        if nx >= 0 or ny >= 0 or nx < n or ny < m:
            if lab[nx][ny] == 0:
                # 방문 처리
                lab[nx][ny] = 2
                dfs(nx, ny)
        

# 지도 입력 받기
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 지도에서 0, 2인 부분의 인덱스 모으기
zero_index = []
two_index = []
save_size = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_index.append((i, j))
        if graph[i][j] == 2:
            two_index.append((i, j))

# 벽을 세워야 할 위치 3개 뽑기
indexes = list(combinations(zero_index, 3))
print(indexes[0:5])
save2 = []
# 그 경우에 수에 해당하는 위치 1로 만들기 (벽 세우기)
for index in indexes:
    # 연구소 지도 초기화
    lab = graph
    lab[index[0][0]][index[0][1]] = 1
    lab[index[1][0]][index[1][1]] = 1
    lab[index[2][0]][index[2][1]] = 1
    count = 0
    save = 0
    ways = [(-1, 0), (1, 0), (0, -1), (0, 1)]
     # 바이러스 퍼뜨리기
    for index_2 in two_index:
        dfs(index_2[0], index_2[1])
        
    for i in range(n):
            for j in range(m):
                if lab[i][j] == 0:
                    save += 1
    save2.append(save)
##        # 0의 개수 세기
        
##        print(lab)
##        print('----------------------------------------')
##        print(save)
    save_size.append(len(zero_index) - count - 3 + 2)
    
print(max(save_size))
print(save_size[:10])
print(max(save2))

# 금광

def get_gold(n, m, array):
    d = [[0]*m for _ in range(n)]
    # 출발지 초기화
    for i in range(n):
        d[i][0] = array[i][0]
    # 오른쪽으로 m번 이동하면 종료
    for i in range(1, m):
        for j in range(n):
            # 열을 모두 채우고 넘어가기
            # 왼쪽 위에서 오는 경우
            # 제일 위에 있으면 pass
            if j != 0:
                d[j][i] = max(d[j][i], d[j - 1][i - 1] + array[j][i])
            # 왼쪽에서 오는 경우
            d[j][i] = max(d[j][i], d[j][i - 1] + array[j][i])
            # 왼쪽 아래에서 오는 경우
            # 제일 아래에 있으면 pass
            if j != (n - 1):
                d[j][i] = max(d[j][i], d[j + 1][i - 1] + array[j][i])
    result = max([d[i][m - 1] for i in range(n)])
    return result


# 금광 개수 입력 받기
t = int(input())
for i in range(t):
    # 금광 크기 입력 받기
    n, m = map(int, input().split())
    # 금광 배열 입력 받기
    array = list(map(int,input().split()))
    # 2차원 배열로 만들기
    array_2 = []
    j = m
    for _ in range(n):
        array_2.append(array[j - 4:j])
        j += m
    print(get_gold(n, m, array_2))


###------------------- 조금 다른 방법 -------------------
##
##def get_gold(n, m, array):
##    d = [[0]*m for _ in range(n)]
##    for i in range(n):
##        d[i][0] = array[i][0]
##    for i in range(1, m):
##        for j in range(n):
##            # 왼쪽 위에서 오는 경우
##            if j != 0:
##                left_up = d[j - 1][i - 1]
##            # 왼쪽에서 오는 경우
##            left = d[j][i - 1]
##            # 왼쪽 아래에서 오는 경우
##            if j != (n - 1):
##                left_down = d[j + 1][i - 1]
##            d[j][i] = max(left_up, left, left_down) + array[j][i]
##    result = max([d[i][m - 1] for i in range(n)])
##    return result
##
##
### 금광 개수 입력 받기
##t = int(input())
##for i in range(t):
##    n, m = map(int, input().split())
##    array = list(map(int,input().split()))
##    
##    # 2차원 배열로 만들기
##    array_2 = []
##    j = m
##    for _ in range(n):
##        array_2.append(array[j - 4:j])
##        j += m
##    print(get_gold(n, m, array_2))
##



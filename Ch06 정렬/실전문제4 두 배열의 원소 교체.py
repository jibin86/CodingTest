# 두 배열의 원소 교체

# n, k 입력 받기
n, k = map(int, input().split())

# 배열 A, B의 원소 입력 받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 최소 원소, B의 최대 원소 찾기

for _ in range(k):
    a = A.index(min(A))
    b = B.index(max(B))
    if A[a] > B[b]:
        break
    A[a], B[b] = B[b], A[a]
    
print(sum(A))

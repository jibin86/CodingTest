# 부품 찾기

def binary_search(array, target, start ,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif target > array[mid]:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

# 가게의 부품 개수 입력 받기
n = int(input())
# 가게에 있는 부품 번호 입력 받기
array = list(map(int, input().split()))

# 요청한 부품 개수 입력 받기
m = int(input())
# 요청한 부품 번호 입력 받기
requested = list(map(int, input().split()))

# 가게 부품 정렬
array.sort()

for target in requested:
    if binary_search(array, target, 0, n-1) :
        print('yes', end=' ')
    else:
        print('no', end=' ')
    

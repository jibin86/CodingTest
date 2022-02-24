# 떡볶이 떡 만들기

# 떡의 개수 n, 요청한 떡의 길이 m 입력받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    leftover = 0
    for i in array:
        if i > mid:
            leftover += (i - mid)
    if leftover == target:
        return mid
    if leftover > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)
    
print(binary_search(array, m, 0, max(array)))

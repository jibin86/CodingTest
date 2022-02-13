#그리디 알고리즘
#문제 : N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력

n, k = map(int, input().split()) # n = 25, k = 3

result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)
    

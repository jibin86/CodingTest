# 1이 될 때까지 : n이 k로 나누어 떨어지면 k로 나누고 아니면 n에 1을 빼는 시행을 반복하여
#                 n이 1이 되도록 하는 횟수를 구하기

import time
n, k = map(int, input().split())

start_time = time.time()

count = 0

while n != 1:
    count += 1
    if n % k == 0:
        n = n / k
    else:
        n = n - 1

print(count)

end_time = time.time()
print("time :", end_time - start_time)

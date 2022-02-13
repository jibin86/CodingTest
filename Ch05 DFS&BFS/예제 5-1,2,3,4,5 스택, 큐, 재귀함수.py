# 리스트 거꾸로 출력 : print(stack[::-1])

#
# --------------------------------스택--------------------------------
#
##stack = []
##
### 5삽입 - 2삽입 - 3삽입 - 7삽입 - 삭제 - 1삽입 - 4삽입 - 삭제
##
##stack.append(5)
##stack.append(2)
##stack.append(3)
##stack.append(7)
##stack.pop()
##stack.append(1)
##stack.append(4)
##stack.pop()
##
##print(stack)
##print(stack[::-1])
##
##
###
### --------------------------------큐--------------------------------
###
##from collections import deque
##
##queue = deque()
##
### 5삽입 - 2삽입 - 3삽입 - 7삽입 - 삭제 - 1삽입 - 4삽입 - 삭제
##
##queue.append(5)
##queue.append(2)
##queue.append(3)
##queue.append(7)
##queue.popleft()
##queue.append(1)
##queue.append(4)
##queue.popleft()
##
##print(queue)
##queue.reverse()
##print(queue)
##
##
###
### --------------------------------재귀 함수--------------------------------
###
##
##def recursive_function(i):
##    if i == 100:
##        return
##    print(i, '번째 재귀 함수를 호출합니다.')
##    recursive_function(i + 1)
##    print(i, '번째 재귀 함수를 종료합니다.')
##
##recursive_function(1)
##
##
###
### --------------------------------팩토리얼--------------------------------
###
##
###반복적으로 구현한 n!
##def factorial_iterative(n):
##    result = 1
##    for i in range(1, n+1):
##        result *= i
##    return result
##
###재귀적으로 구현한 n!
##def factorial_recursive(n):
##    if n <= 1:
##        return 1
##    return n * factorial_recursive(n-1)
##
##print(factorial_iterative(5))
##print(factorial_recursive(5))
##    

# 최대공약수 계산 (유클리드 호제법)

def GCD(a, b):
    if(a % b == 0):
        return b
    r = a % b
    return GCD(b, r)

print(GCD(192, 162))












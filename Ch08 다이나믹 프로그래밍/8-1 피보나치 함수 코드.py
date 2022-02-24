# 피보나치 함수를 재귀함수로 구현
# x는 항 순서 나타냄
def fibo(x):
    # 종료 조건 설정
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print('찾고 싶은 피보나치 수열의 항 번호를 입력하세요')
print('n = ', end=' ')
n = int(input())
print(fibo(n))

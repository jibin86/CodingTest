# 바닥 공사 (보텀업)
n = int(input())

# DP 테이블 생성
d = [0] * 1001

# 초기화 설정
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 2] * 2 + d[i - 1]) % 796796

print(d[n])

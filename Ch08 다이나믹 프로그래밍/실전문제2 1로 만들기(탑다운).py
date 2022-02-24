# 1로 만들기 탑다운 방식 (재귀적)

n = int(input())

# 메모이제이션: 최소 가짓수 기록
d = [0] * 100
def make_one(x):
    # 종료 조건
    if x == 1:
        return d[x]

    # 이전 단계가 기록된 문제라면 모두 앞 단계 가짓 수에 1을 더한 것과 기존의 것 비교해서 작은 것 선택
    if d[x-1] != 0:
        d[x] = d[x-1] + 1
        if x % 2 == 0:
            d[x] = min(d[x], d[x // 2] + 1)
        if x % 3 == 0:
            d[x] = min(d[x], d[x // 3] + 1)
        if x % 5 == 0:
            d[x] = min(d[x], d[x // 5] + 1)
        return d[x]

    # 이전 단계가 기록되지 않은 문제라면 재귀적으로 함수 호출해서 점화식 계산  
    d[x] = make_one(x - 1) + 1
    if x % 2 == 0:
        d[x] = min(d[x], make_one(x // 2) + 1)
    if x % 3 == 0:
        d[x] = min(d[x], make_one(x // 3) + 1)
    if x % 5 == 0:
        d[x] = min(d[x], make_one(x // 5) + 1)
    return d[x]

print(make_one(n))

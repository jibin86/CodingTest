import itertools

n, m = map(int, input().split())
balls = list(map(int, input().split()))

same_cnt = 0
# 조합
nCr = list(itertools.combinations(balls, 2))
for p in nCr:
  if p[0] == p[1]:
    same_cnt += 1

print(len(nCr) - same_cnt)
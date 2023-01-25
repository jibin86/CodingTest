# 수정된 코드
n = int(input())
coin = list(map(int, input().split()))
coin.sort()
target = 1
for c in coin:
  if c <= target:
    target += c
  else:
    print(target)
    


# import itertools

# n = int(input())
# coin = list(map(int, input().split()))

# # 작은 수가 앞에 오도록 정렬
# coin.sort()  # 1 1 2 3 9

# f = False
# # 양의 정수 금액이므로 1부터 만들어본다.
# for i in range(1, max(coin) + 2):
#   if i in coin:
#     continue
#   # 동전 리스트에 없다면 조합해서 4가 되는지 확인

#   # 4보다 작은 수 찾기
#   for j in coin:
#     # if 합이 4보다 작으면 정답
#     if j > i:
#       m_idx = coin.index(j) - 1
#       break
#   print('hi')
#   print(m_idx)
#   # 모든 조합 중에서 4가 있으면 다음 정수로
#   for l in range(2, m_idx + 2):
#     print(f'target {i}, {l}개 조합')
#     for k in list(itertools.combinations(coin[: m_idx + 1], l)):
#       print(k,sum(k))
#       if sum(k) == i:
#         f = True
#         print('middle',i)
#         break
#     if f:
#       break
#   if f:
#     print('go to next')
#     f = False
#     continue 
#   print('result',i)
#   break

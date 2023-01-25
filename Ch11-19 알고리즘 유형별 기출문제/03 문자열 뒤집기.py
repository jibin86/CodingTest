# 문자열 s입력받기
s = list(map(int, list(input())))  # map은 list()를 씌워야한다

# 연속된 수를 하나의 수로 취급한다.
group = []
# 리스트에 문자열 앞 숫자를 집어넣고 before(s[i-1])와 now(s[i])가 다르면 now 숫자를 집어 넣는다.
# 같으면 before과 now를 한 칸 이동시킨다.
group.append(s[0])
for i in range(1, len(s)):
  if s[i - 1] != s[i]:
    group.append(s[i])
if len(group) == 1:
  print(0)
else:
  # 가장 빈도가 적은 원소
  print(group.count(min(set(group), key=group.count)))

# 리스트를 입력받아서 빈도수가 가장 높은 요소 출력하는 프로그램
# def most_frequent(data):
#     return max(data, key=data.count)

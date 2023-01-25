n = list(input())
n.sort()
int_list = []
str_list = []
for i in range(len(n)):
  try:
    int(n[i])
    int_list.append(int(n[i]))
  except:
    str_list.append(n[i])
    continue

print("".join(str_list) + str(sum(int_list)))

# 책 코드
n = list(input())
n.sort()
int_value = 0
result = []
for i in n:
  # 알파벳인 경우 결과 리스트에 삽입
  if i.isalpha():
    result.append(i)
  # 숫자는 따로 더하기
  else:
    int_value += int(i)
# 알파벳 오름차순으로 정렬
str_list.sort()

if int_value != 0:
  result.append(str(int_value))
print(''.join(result))
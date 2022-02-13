# 왕실의 나이트
# 아스키코드 A ~ Z -> 65 ~ 90
#            a ~ z -> 97 ~ 122
# 문자 -> 아스키코드 : ord(문자)
# 아스키코드 -> 문자 : chr(아스키)
# 데이터 타입 확인 : type()

# x, y 좌표 할당하기
location = input()
x = int(location[1])
y = ord(location[0])-int(ord('a')) + 1

count = 0
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1
print(count)


# 다른 방법

count = 0
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (-2,1), (-1,2), (1,2), (2,1)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    count += 1
print(count)

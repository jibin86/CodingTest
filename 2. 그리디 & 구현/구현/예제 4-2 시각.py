# 시각
# 정수를 문자열로 변환 : str()
# 주석 단축키 : idle-> alt + 3 (주석 처리), alt + 4 (주석 해제), 나머지 편집기 -> ctrl + / (주석 처리)
# 커서 가장 위로 : ctrl + home
# 커서 가장 밑으로 : ctrl + end

n = int(input())

count = 0
# 시, 분, 초 순으로 3이 있나 확인
for hour in range(n+1):
    if '3' in str(hour):
            count += 3600
    else:
        for minute in range(60):
            if '3' in str(minute):
                count += 60
            else:
                for second in range(60):
                    if '3' in str(second):
                        count += 1
print(count)
            
# 다른 방법 : 매 시각을 문자열로 바꾼 다음 문자열에 '3' 이 포함되었는지 검사한다.

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

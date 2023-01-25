import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    print(q)
    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 시간
    previous = 0

    # 남은 음식의 개수
    length = len(food_times)

    # (먹기 위해 사용한 시간) + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    # k보다 적은 시간일 때
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 새롭게 가장 적은 시간을 가진 음식 꺼내기
        print(q)
        sum_value += (now - previous) * length # 지금까지 먹는데 사용한 시간
        length -= 1 # 다 먹은 음식 제외
        previous = now # previous에 가장 적은 시간을 가진 음식 담기

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) # 음식 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]
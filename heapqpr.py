# from queue import PriortyQueue - 쓰레드 안전이 걸려있음(속도 ↓)
# 힙으로 구현을 합니다.
import heapq as hq

min_heap = []  # heap 으로 사용할 list
hq.heappush(min_heap, 456)
hq.heappush(min_heap, 478)
hq.heappush(min_heap, 41)
hq.heappush(min_heap, 123)
hq.heappush(min_heap, 789)
hq.heappush(min_heap, 478)  #
print(min_heap)    # 순서대로 출력되지 않는 것을 확인할 수 있습니다.
print("size:", len(min_heap))
while min_heap:
    print(hq.heappop(min_heap))  # list pop

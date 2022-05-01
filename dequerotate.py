from collections import deque

# Contains 1,2,3,4,5 in deq
deq = deque([1,2,3,4,5])

deq.rotate(1)
print(deq)
# deque([5,1,2,3,4])
deq.rotate(-1)
print(deq)
# deque([1,2,3,4,5])

#양수 값 또는 음수 값을 파라미터로 제공하여 데크를 좌 우로 회전 할 수 있다.



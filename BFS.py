from collections import deque

#BFS 메서드 정의
def bfs(graph, start,visited) :
# 큐 구현을 위하여 deque 라이브러리 사용
    queue = deque([start])

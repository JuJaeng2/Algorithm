# 우선순위 큐의 Starvation(기아)현상을 보완

import heapq
# 
import random

class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

# 우선순위 큐 생성
queue = []
cnt = 0
name = 3
# 작업 추가
heapq.heappush(queue, Job(5, "작업 1"))
heapq.heappush(queue, Job(3, "작업 2"))
heapq.heappush(queue, Job(7, "작업 3"))

# 작업 처리
# while루프를 사용하여 우선순위 큐가 비어있지 않은 동안 작업을 처리
while queue:
    # heapq.heappop()함수를 사용하여 우선순위가 가장 높은 작업을 큐에서 가져온다.
    # 이 작업을 job변수에 저장하고 작업의 설명을출력
    job = heapq.heappop(queue)
    print(f"Processing: {job.description} // Priority : {job.priority}")
    cnt += 1
    
    # 중간에 새로운 작업이 들어올 경우를 만들어줌
    if cnt%3 == 0:
        name += 1
        if name < 6:
            pr = random.randrange(1,4)
            heapq.heappush(queue, Job(pr, "추가된 작업 "+str(name)))

    # 작업 처리 후 우선순위 조정
    # 작업의 우선순위가 1보다 큰 경우, 우선순위를 1 감소시킨 후 다시 우선순위 큐에 추가
    # 작업들의 우선순위가 동적으로 조정되며, 기아 현상을 해결
    if job.priority > 1:
        # 작업의 우선순위를 감소
        job.priority -= 1
        # 작업을 다시 큐에 추가
        heapq.heappush(queue, job)

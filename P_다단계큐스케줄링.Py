# 다단계 큐를 나타내는 클래스

class MultiLevelQueue:
    # 클래스의 인스턴스가 생성될 때 호출되는 초기화 메서드
    # queue변수는 3개의 우선순위 큐를 빈 리스트로 초기화
    def __init__(self):
        self.queues = [[] for _ in range(3)]  # 3개의 우선순위 큐

    # 프로세스와 우선순위를 인자로 받아 해당 우선순위의 큐에 프로세스를 추가
    # queue리스트의 인덱스는 우선순위를 나타내며, 해당 인덱스에 프로세스를 추가
    def enqueue(self, process, priority):
        self.queues[priority].append(process) # 주어진 우선순위에 해당하는 큐에 프로세스 추가

    # 가장 낮은 우선순위 큐부터 순서대로 확인하여 큐에서 프로세스를 꺼내고 반환
    # 각 큐에서는 가장 앞에 있는 프로세스를 꺼내기 위해 pop(0) 메서드를 사용
    # 만약 모든 큐가 비어있는 경우 None을 반환
    def dequeue(self):
        for queue in self.queues:
            if queue:
                return queue.pop(0) # 가장 높은 우선순위 큐부터 순서대로 확인하여 프로세스를 꺼내고 변환
        return None # 모든 큐가 비어있을 경우 None 반환

# scheduler객체 생성
scheduler = MultiLevelQueue()

# enqueue메서드를 사용하여 프로세스를 큐에 추가
scheduler.enqueue("Process A", 0)  # 낮은 우선순위 큐
scheduler.enqueue("Process B", 1)  # 중간 우선순위 큐
scheduler.enqueue("Process C", 2)  # 높은 우선순위 큐
scheduler.enqueue("Process D", 0)  # 낮은 우선순위 큐
scheduler.enqueue("Process E", 1)  # 중간 우선순위 큐
scheduler.enqueue("Process F", 2)  # 높은 우선순위 큐
scheduler.enqueue("Process G", 0)  # 낮은 우선순위 큐
scheduler.enqueue("Process H", 1)  # 중간 우선순위 큐
scheduler.enqueue("Process I", 2)  # 높은 우선순위 큐


# 프로세스를 큐에서 꺼내기
while True:
    # 큐의 진행 상황 출력
    for i, queue in enumerate(scheduler.queues):
        print(f"Queue {i}:", queue)
    process = scheduler.dequeue()
    if process:
        print("Processing:", process)
    else:
        break


# < 다단계 큐의 문제점>
# 1.복잡성
# 다단계 큐 스케줄링은 여러 개의 큐를 관리해야 하기 때문에 구현 및 유지 관리가 복잡
# 각 큐에 대한 우선순위 및 스케줄링 알고리즘을 정의해야 하며, 이는 시스템의 복잡성을 증가시킴
# 2. 오버헤드
# 다단계 큐 스케줄링은 프로세스를 여러 큐에 분류하고 이동시키는 작업이 필요
# 이는 프로세스 간의 전환이나 쿠 간의 이동에 따른 오버헤드를 초래할 수 있음 
# 이로인해 시스템의 성능이 저하될 수 있음
# 3. 자원 이용의 불균형
# 다단계 큐 스케줄링은 프로세스를 우선순위에 따라 다른 큐에 할당
# 그러나 우선순위에 따라 프로세스가 분류되는 경우 특정 큐에 자원이 과도하게 지중될 수 있음
# 이로 인해 일부 큐는 비어있는 상태로 유지되거나 자원 불균형이 발생할 수 있음
# 4. Starvation(기아) 문제
# 다단계 큐 스케줄링에서는 높은 우선순위를 가진 프로세스가 낮은 우선순위를 가진 프로세스보다 우선적으로 처리됨
# 이로인해 낮은 우선순위읜 프로세스는 오랜 시간 동안 기다려야 할 수 있으며, 스타베이션 현상이 발생할 수 있음
# 이는 낮은 우선순위 프로세스의 응답 시간을 지연시키고 시스템의 전반적인 성능을 저하시킬 수 있음
# 5. 우선순위 반전
# 다단계 큐 스케줄링에서는 우선순위가 높은 프로세스가 낮은 우선순위의 프로세스보다 우선적으로 처리됨
# 그러나 높은 우선순위의 프로세스가 자원을 오랜 시간 동안 점유하는 경우, 낮은 우선순위의 프로세스가 대기해야 할 수 있음
# 이는 우선순위 반전 문제를 야기할 수 있음

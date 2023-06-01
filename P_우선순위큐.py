#heapq모듈 사용
import heapq
import random

# 작업 클래스 정의
# 어떤 작업이 어느정도의 우선순위를 가지고 있는지 알기 위해서 클래스 사용하고 우선순위 비교
class Job:
    # __init__ 메소드 : 작업의 이름과 우선순위를 초기화
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    # 작업 우선순위 비교를 위한 매직 메소드
    # __lt__ 메소드 : 객체간의 우선순위를 비교할 때 사용
    # 이 메서드를 오버라이딩하여 작업들을 우선순위로 비교할 수 있다.
    def __lt__(self, other):
        return self.priority < other.priority


# 작업 생성
# Job클래스의 객체를 생성하여 각 작업을 정의한다.
# 작업 이름과 우선순위를 인자로 전달하여 초기화한다.
# 값들을 job_list에 넣어준다.
job_list = []
job_list.append(Job("Job 1", 6))
job_list.append(Job("Job 2", 4))
job_list.append(Job("Job 3", 2))
job_list.append(Job("Job 4", 1))
job_list.append(Job("Job 5", 7))
job_list.append(Job("Job 6", 3))
job_list.append(Job("Job 7", 5))
job_list.append(Job("Job 8", 8))


# 우선순위 큐 생성 및 작업 추가
# priority_queue는 우선순위 큐를 나타내는 리스트
# heapq.heappush 함수를 사용하여 작업을 큐에 추가한다.
# 이 함수는 작업을 우선순위 따라 저열된 상태로 유지한다.
priority_queue = []
for job in job_list:
    heapq.heappush(priority_queue, job)


cnt = 0
name = 8
# 작업 처리
# while루프를 사용하여 priority_queue가 비어있을 때 까지 작업을 처리한다.
# heqpq.heqppop함수를 사용하여 가장 우선순위가 높은 작업을 큐에서 제거하고 반환한다.
# 작업의 이름과 우선순위를 출력한다
while priority_queue:
    job = heapq.heappop(priority_queue)
    print(f"현재 처리중인 작업의 이름 : {job.name} => 우선순위 : {job.priority}")

    # 추가작업 입력(랜덤으로 우선순위값을 가진다.)
    if cnt%3 == 0:
        name += 1
        if name < 12:
            pr = random.randrange(1,10)
            heapq.heappush(priority_queue, Job("New Job " + str(name), pr))

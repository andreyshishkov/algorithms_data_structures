import heapq


def main():
    n, m = (int(x) for x in input().split())
    processors = []
    for i in range(n):
        heapq.heappush(processors, (0, i))

    operation_times = (int(x) for x in input().split())
    for task_time in operation_times:
        proc = heapq.heappop(processors)
        print(proc[1], proc[0])
        heapq.heappush(processors, (proc[0] + task_time, proc[1]))


if __name__ == '__main__':
    main()

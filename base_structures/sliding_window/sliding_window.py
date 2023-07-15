from typing import List
from collections import deque


def get_maximums(arr: List[int], m: int, n: int) -> List[int]:
    queue = deque()
    maximums = []

    for i in range(m):
        while queue and arr[i] >= arr[queue[-1]]:
            queue.pop()

        queue.append(i)

    for i in range(m, n):
        maximums.append(arr[queue[0]])

        while queue and queue[0] <= i - m:
            queue.popleft()

        while queue and arr[i] >= arr[queue[-1]]:
            queue.pop()

        queue.append(i)

    maximums.append(arr[queue[0]])
    return maximums


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    m = int(input())
    maximums = get_maximums(arr, m, n)
    print(*maximums)


if __name__ == '__main__':
    main()

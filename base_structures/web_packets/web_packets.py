from collections import deque


def main():
    size, n = (int(x) for x in input().split())
    arrival = []
    duration = []
    for _ in range(n):
        arr_i, dur_i = (int(x) for x in input().split())
        arrival.append(arr_i)
        duration.append(dur_i)

    buffer = deque()
    for i in range(n):

        if len(buffer) == 0:
            finish_time = arrival[i] + duration[i]
            buffer.append(finish_time)
            print(arrival[i])
            continue

        if arrival[i] < buffer[0]:
            if len(buffer) == size:
                print(-1)
            else:
                finish_time = buffer[-1] + duration[i]
                print(buffer[-1])
                buffer.append(finish_time)
        else:
            buffer.popleft()
            finish_time = buffer[-1] + duration[i] if buffer else arrival[i] + duration[i]
            start_time = max(buffer[-1], arrival[i]) if buffer else arrival[i]
            print(start_time)
            buffer.append(finish_time)


if __name__ == '__main__':
    main()

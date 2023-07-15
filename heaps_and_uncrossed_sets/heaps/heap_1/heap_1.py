from typing import List


class Heap:
    def __init__(self, arr: List[int]):
        self.heap = arr
        self.exchanges = []

    @staticmethod
    def get_parent_id(i: int):
        index = (i - 1) // 2
        return index

    @staticmethod
    def get_left_child_id(i: int):
        index = 2 * i + 1
        return index

    @staticmethod
    def get_right_child_id(i: int):
        index = 2 * i + 2
        return index

    def shift_down(self, i):
        max_i = i
        left_child_id = self.get_left_child_id(i)
        if left_child_id < len(self.heap) and self.heap[left_child_id] < self.heap[max_i]:
            max_i = left_child_id

        right_child_id = self.get_right_child_id(i)
        if right_child_id < len(self.heap) and self.heap[right_child_id] < self.heap[max_i]:
            max_i = right_child_id

        if i != max_i:
            self.exchanges.append((i, max_i))
            self.heap[i], self.heap[max_i] = self.heap[max_i], self.heap[i]
            self.shift_down(max_i)

    def build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.shift_down(i)


def main():
    _ = int(input())
    arr = [int(x) for x in input().split()]
    heap = Heap(arr)
    heap.build_heap()

    m = len(heap.exchanges)
    print(m)
    if m:
        for x1, x2 in heap.exchanges:
            print(x1, x2)


if __name__ == '__main__':
    main()

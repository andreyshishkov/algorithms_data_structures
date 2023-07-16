from typing import List


def find(i: int, parent: List[int]) -> int:
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(i: int, j: int, parent: List[int], rank: List[int]):
    parent_i = find(i, parent)
    parent_j = find(j, parent)

    if parent_j == parent_i:
        return

    if rank[parent_i] > rank[parent_j]:
        parent[parent_j] = parent_i
    else:
        parent[parent_i] = parent_j
        if rank[parent_i] == rank[parent_j]:
            rank[parent_j] += 1


def main():
    n, e, d = (int(x) for x in input().split())
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    answer = 1
    for _ in range(e):
        i, j = (int(x) for x in input().split())
        union(i - 1, j - 1, parent, rank)

    for _ in range(d):
        p, q = (int(x) for x in input().split())
        p_id = find(p - 1, parent)
        q_id = find(q - 1, parent)

        if p_id == q_id:
            answer = 0
            break
    print(answer)


if __name__ == '__main__':
    main()

from typing import List


def find(i: int, parent: List[int]) -> int:
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(destination: int, source: int, parent: List[int], rank: List[int], max_rank: int) -> int:
    destination_parent = find(destination, parent)
    source_parent = find(source, parent)

    if destination_parent != source_parent:
        parent[source_parent] = destination_parent
        rank[destination_parent] += rank[source_parent]

        max_rank = max(max_rank, rank[destination_parent])

    return max_rank


def main():
    n, m = (int(x) for x in input().split())
    ranks = [int(x) for x in input().split()]

    parents = [i for i in range(n)]
    max_rank = max(ranks)

    for _ in range(m):
        destination_i, source_i = (int(x) for x in input().split())
        max_rank = union(destination_i - 1, source_i - 1, parents, ranks, max_rank)
        print(max_rank)


if __name__ == '__main__':
    main()

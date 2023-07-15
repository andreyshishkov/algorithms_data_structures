import sys
from collections import defaultdict
from typing import List, Dict, Tuple

sys.setrecursionlimit(20000)


def get_tree(parents: List[int]) -> Tuple[Dict[int, List[int]], int]:
    tree = defaultdict(list)
    root = -1
    for i, node in enumerate(parents):
        if node != -1:
            tree[node].append(i)
        else:
            root = i
    return tree, root


def get_height(tree, root) -> int:
    height = 1
    for node in tree[root]:
        height = max(height, 1 + get_height(tree, node))
    return height


def main():
    _ = int(input())
    parents = [int(x) for x in input().split()]
    tree, root = get_tree(parents)
    result = get_height(tree, root)
    print(result)


if __name__ == '__main__':
    main()

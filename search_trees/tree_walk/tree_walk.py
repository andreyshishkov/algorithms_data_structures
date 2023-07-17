from typing import List


class Node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None


def pre_order(root: Node, arr: List[int] = None) -> List[int]:
    if arr is None:
        arr = []
    key = root.key
    arr.append(key)
    if root.left:
        pre_order(root.left, arr)
    if root.right:
        pre_order(root.right, arr)

    return arr


def post_order(root: Node, arr: List[int] = None) -> List[int]:
    if arr is None:
        arr = []

    if root.left:
        post_order(root.left, arr)
    if root.right:
        post_order(root.right, arr)

    arr.append(root.key)

    return arr


def in_order(root: Node, arr: List[int] = None) -> List[int]:
    if arr is None:
        arr = []

    if root.left:
        in_order(root.left, arr)

    arr.append(root.key)

    if root.right:
        in_order(root.right, arr)

    return arr


def main():
    n = int(input())
    nodes = [Node() for _ in range(n)]
    for i in range(n):
        key, left, right = (int(x) for x in input().split())
        nodes[i].key = key
        if left != -1:
            nodes[i].left = nodes[left]
        if right != -1:
            nodes[i].right = nodes[right]

    in_order_result = in_order(nodes[0])
    print(*in_order_result)

    pre_order_result = pre_order(nodes[0])
    print(*pre_order_result)

    post_order_result = post_order(nodes[0])
    print(*post_order_result)


if __name__ == '__main__':
    main()

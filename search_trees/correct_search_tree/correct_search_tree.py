import sys
sys.setrecursionlimit(100000)


class Node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None


def check(node: Node, min_: int = None, max_: int = None) -> bool:
    if min_ is None:
        min_ = -float('+inf')
        max_ = float('+inf')
    if node is None:
        return True
    if node.key <= min_ or node.key >= max_:
        return False
    return check(node.left, min_, node.key) and check(node.right, node.key, max_)


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

    if nodes:
        result = 'CORRECT' if check(nodes[0]) else 'INCORRECT'
        print(result)
    else:
        print('CORRECT')


if __name__ == '__main__':
    main()

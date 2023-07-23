from typing import Union


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.sum = key


class AvlTree:

    @staticmethod
    def get_max(node: Node):
        cur_node = node
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node

    @staticmethod
    def get_min(node: Node):
        cur_node = node
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    @staticmethod
    def get_height(node: Node):
        return node.height if node else 0

    @staticmethod
    def get_sum(node: Node):
        return node.sum if node else 0

    def get_balance_factor(self, node: Node):
        if node is None:
            return 0
        return self.get_height(node.right) - self.get_height(node.left)

    def update_height(self, node: Node):
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def update_sum(self, node: Node):
        node.sum = self.get_sum(node.left) + self.get_sum(node.right) + node.key

    def update(self, node: Node):
        self.update_sum(node)
        self.update_height(node)

    def rotate_left(self, node: Node):
        top_node = node.right
        if top_node:
            node.right = top_node.left
            top_node.left = node
            self.update(node)
            self.update(top_node)
            return top_node
        return node

    def rotate_right(self, node: Node):
        top_node = node.left
        if top_node:
            node.left = top_node.right
            top_node.right = node
            self.update(node)
            self.update(top_node)
            return top_node
        return node

    def balance(self, node: Node):
        """Balance AVL-tree"""
        if node is None:
            return None
        self.update(node)

        if self.get_balance_factor(node) > 1:
            if self.get_balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)

        if self.get_balance_factor(node) < -1:
            if self.get_balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)

        return node if -1 <= self.get_balance_factor(node) <= 1 else self.balance(node)

    def find(self, key, node):
        """Find node using key"""
        if node is None:
            return
        if node.key == key:
            return node
        elif node.key > key:
            return self.find(key, node.left)
        else:
            return self.find(key, node.right)

    def add(self, key, node) -> Node:
        """Add new node to tree"""
        if node is None:
            return Node(key)

        if node.key > key:
            node.left = self.add(key, node.left)
        elif node.key < key:
            node.right = self.add(key, node.right)
        return self.balance(node)

    def __remove_min(self, node):
        if node.left is None:
            return node.right
        node.left = self.__remove_min(node.left)
        return self.balance(node)

    def remove(self, key: int, node: Node) -> Union[Node, None]:
        """Remove node from tree"""
        if node is None:
            return

        if node.key > key:
            node.left = self.remove(key, node.left)

        elif node.key < key:
            node.right = self.remove(key, node.right)

        else:
            left_node = node.left
            right_node = node.right
            del node
            if right_node is None:
                return left_node
            min_node = self.get_min(right_node)
            min_node.right = self.__remove_min(right_node)
            min_node.left = left_node
            return self.balance(min_node)

        return self.balance(node)


class IntervalSet:
    def __init__(self):
        self.s = 0
        self.current_node = None
        self.avl_tree = AvlTree()

    def __func(self, value: int) -> int:
        return (value + self.s) % 1_000_000_001

    # base operations
    def add(self, num: int) -> Node:
        self.current_node = self.avl_tree.add(self.__func(num), self.current_node)
        return self.current_node

    def find(self, num: int) -> str:
        return 'Found' if self.avl_tree.find(self.__func(num), self.current_node) else 'Not found'

    def remove(self, num: int) -> Node:
        self.current_node = self.avl_tree.remove(self.__func(num), self.current_node)
        return self.current_node

    def sum(self, left: int, right: int):
        if self.current_node is None:
            self.s = 0
        else:
            s = self.__interval(self.__func(left), self.__func(right), self.current_node)
            self.s = s if s else 0
        return self.s

    # operations for interval sum
    def __cut_right(self, key: int, node: Node) -> Union[Node, None]:
        if node.right is None:
            return None
        if node.right.key >= key:
            return node.right
        return self.__cut_right(key, node.right)

    def __cut_left(self, key: int, node: Node) -> Union[Node, None]:
        if node.left is None:
            return None
        if node.left.key <= key:
            return node.left
        return self.__cut_left(key, node.left)

    def __sub_over_nodes(self, key, sum_: int, node: Node):
        if node is None:
            return sum_
        if node.key <= key:
            return self.__sub_over_nodes(key, sum_, node.right)
        else:
            sum_ -= node.sum
            sum_ = self.__add_lower_and_same_nodes(key, sum_, node.left)
            return sum_

    def __add_lower_and_same_nodes(self, key: int, sum_: int, node: Node) -> int:
        if node is None:
            return sum_

        if node.key > key:
            return self.__add_lower_and_same_nodes(key, sum_, node.left)
        sum_ += node.sum
        sum_ = self.__sub_over_nodes(key, sum_, node.right)
        return sum_

    def __sub_lower_nodes(self, key: int, sum_: int, node: Node) -> int:
        if node is None:
            return sum_
        if node.key >= key:
            return self.__sub_lower_nodes(key, sum_, node.left)
        sum_ -= node.sum
        sum_ = self.__add_over_and_same_nodes(key, sum_, node.right)
        return sum_

    def __add_over_and_same_nodes(self, key: int, sum_: int, node: Node) -> int:
        if node is None:
            return sum_
        if node.key < key:
            return self.__add_over_and_same_nodes(key, sum_,    node.right)

        sum_ += node.sum
        sum_ = self.__sub_lower_nodes(key, sum_, node.left)
        return sum_

    def __sub_left(self, key: int, sum_: int, node: Node) -> int:
        if node.key <= key:
            sum_ -= node.sum
            return self.__add_over_and_same_nodes(key, sum_, node)
        if node.left is None:
            return sum_
        return self.__sub_left(key, sum_, node.left)

    def __sub_right(self, key: int, sum_: int, node: Node) -> int:
        if node.key >= key:
            sum_ -= node.sum
            return self.__add_lower_and_same_nodes(key, sum_, node)
        if node.right is None:
            return sum_
        return self.__sub_right(key, sum_, node.right)

    def __interval(self, left: int, right: int, node: Node) -> int:
        if node is None:
            return 0
        if left <= node.key <= right:

            # sub values which is less than left
            left_node = self.__cut_left(left, node)
            sum_ = self.avl_tree.get_sum(node) - self.avl_tree.get_sum(left_node)
            sum_ = self.__add_over_and_same_nodes(left, sum_, left_node)

            # sub values which is more than right
            right_node = self.__cut_right(right, node)
            sum_ = sum_ - self.avl_tree.get_sum(right_node)
            sum_ = self.__add_lower_and_same_nodes(right, sum_, right_node)

            return sum_

        elif node.key < left:
            sub_tree = self.__cut_right(left, node)
            if sub_tree is None:
                return 0
            sum_ = self.__sub_lower_nodes(left, sub_tree.sum, sub_tree)
            return self.__sub_right(right, sum_, sub_tree)
        elif node.key > right:
            sub_tree = self.__cut_left(right, node)
            if sub_tree is None:
                return 0
            sum_ = self.__sub_over_nodes(right, sub_tree.sum, sub_tree)
            return self.__sub_left(left, sum_, sub_tree)


def main():
    n = int(input())
    interval_set = IntervalSet()
    for _ in range(n):
        commands = input().split()
        if commands[0] == '+':
            num = int(commands[1])
            interval_set.add(num)

        elif commands[0] == '-':
            num = int(commands[1])
            interval_set.remove(num)

        elif commands[0] == '?':
            num = int(commands[1])
            print(interval_set.find(num))

        else:
            left = int(commands[1])
            right = int(commands[2])
            print(interval_set.sum(left, right))


if __name__ == '__main__':
    main()

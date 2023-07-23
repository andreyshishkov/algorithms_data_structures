from typing import Union, Tuple


class Node:

    def __init__(self, value: str = None,  size: int = None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.size = size if size is not None else len(value)


class Rope:

    MAX_LENGTH = 32 # max length of string in Node

    @staticmethod
    def __get_height(node: Node) -> int:
        return node.height if node is not None else 0

    @staticmethod
    def __get_size(node: Node) -> int:
        return node.size if node is None else 0

    def __update_height(self, node: Node):
        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1

    def __update_size(self, node: Node):
        node.size = self.__get_size(node.left) + self.__get_size(node.right)

    def __update(self, node: Node):
        self.__update_height(node)
        self.__update_size(node)

    def __get_balance_factor(self, node) -> int:
        if node is None:
            return 0
        return self.__get_height(node.right) - self.__get_height(node.left)

    def __rotate_left(self, node: Node) -> Node:
        top_node = node.right
        if top_node:
            node.right = top_node.left
            top_node.left = node
            self.__update(node)
            self.__update(top_node)
            return top_node
        return top_node

    def __rotate_right(self, node: Node) -> Node:
        top_node = node.left
        if top_node:
            node.left = top_node.right
            top_node.right = node
            self.__update(node)
            self.__update(top_node)
            return top_node
        return node

    def balance(self, node: Node) -> Union[Node, None]:
        if node is None:
            return
        self.__update(node)

        if self.__get_balance_factor(node) > 1:
            if self.__get_balance_factor(node.left) < 0:
                node.right = self.__rotate_right(node.right)
            self.__rotate_left(node)

        elif self.__get_balance_factor(node) < -1:
            if self.__get_balance_factor(node.right) > 0:
                node.left = self.__rotate_left(node.left)
            self.__rotate_right(node)

        return node if -1 <= self.__get_balance_factor(node) <= 1 else self.balance(node)

    def find(self, key: int, node) -> str:
        if node.left is not None:
            if self.__get_size(node.left) < key:
                return self.find(key - node.left.size, node.right)
            else:
                return self.find(key, node.left)

        return node.value[key]

    def add(self, value: str, node: Node = None):
        if node is None:
            return Node(value=value)

        node.right = self.add(value, node.right)
        return self.balance(node)

    def transform_to_string(self, node: Node, string: str = '') -> str:
        if node is not None:
            new_string = self.transform_to_string(node.left, string)
            if node.value is not None:
                new_string += node.value
            new_string = self.transform_to_string(node.right, new_string)
            return new_string
        return  string

    def merge(self, node1: Node, node2: Node) -> Node:
        if node1 is None:
            return node2
        elif node2 is None:
            return node1

        size = self.__get_size(node1) + self.__get_size(node2)
        if size <= self.MAX_LENGTH:
            return Node(value=self.transform_to_string(node1) + self.transform_to_string(node2))
        merged_node = Node(size=size)
        merged_node.left = node1
        merged_node.right = node2
        return self.balance(merged_node)

    def split(self, key: int, node: Node) -> Tuple[Node, Node]:
        if node.left is not None:
            if self.__get_size(node.left) >= key:
                first, second = self.split(key, node.left)
                tree1 = first
                tree2 = self.merge(second, node.right)
            else:
                first, second = self.split(key - self.__get_size(node.left), node.right)
                tree1 = self.merge(node.left, first)
                tree2 = second

        else:
            prefix = node.value[:key]
            postfix = node.value[key:]
            tree1 = Node(value=prefix) if prefix else None
            tree2 = Node(value=postfix) if postfix else None

        return tree1, tree2

    def insert(self, key: int, node: Node, inserted_node: Node) -> Node:
        if key == 0:
            return self.merge(inserted_node, node)
        elif key >= node.size:
            return self.merge(node, inserted_node)
        prefix, postfix = self.split(key, node)
        return self.merge(self.merge(prefix, inserted_node), postfix)

    def reorder(self, start: int, finish: int, position: int, node: Node) -> Node:
        if start < 0:
            start = 0
        if finish >= node.size:
            return node

        if start == 0:
            sub_str, string = self.split(finish + 1, node)
        else:
            prefix, sub_str = self.split(start, node)
            sub_str, postfix = self.split(finish - start + 1, sub_str)
            string = self.merge(prefix, postfix)
        result_node = self.insert(position, string, sub_str)
        return result_node


def main():
    string = input()
    rope = Rope()
    roped_s = rope.add(string)
    q = int(input())
    for _ in range(q):
        start, finish, position = (int(x) for x in input().split())
        roped_s = rope.reorder(start, finish, position, roped_s)

    print(rope.transform_to_string(roped_s))


if __name__ == '__main__':
    main()

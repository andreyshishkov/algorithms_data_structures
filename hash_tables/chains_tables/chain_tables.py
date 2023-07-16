from typing import List


class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Table:

    def __init__(self, m: int):
        self.p = 1_000_000_007
        self.x = 263
        self.m = m
        self.table = [None for _ in range(m)]

    def get_hash(self, string: str) -> int:
        value = 0
        for i in range(len(string)):
            value += ord(string[i]) * (self.x ** i) % self.p
        value = value % self.p
        value = value % self.m
        return value

    def add(self, string: str):
        if self.find(string):
            return

        table_id = self.get_hash(string)
        if self.table[table_id] is None:
            self.table[table_id] = Node(string)

        else:
            new_node = Node(string)
            last_node = self.table[table_id]

            new_node.next = last_node
            last_node.previous = new_node
            self.table[table_id] = new_node

    def find(self, string: str) -> bool:
        table_id = self.get_hash(string)

        if self.table[table_id] is None:
            return False

        cur_node = self.table[table_id]
        while cur_node:
            if cur_node.value == string:
                return True
            cur_node = cur_node.next
        return False

    def delete_key(self, string: str):
        table_id = self.get_hash(string)
        if self.table[table_id] is None:
            return

        cur_node = self.table[table_id]
        while cur_node:
            if cur_node.value == string:
                if cur_node.previous is None:
                    next_node = cur_node.next
                    if next_node is not None:
                        next_node.previous = None
                    self.table[table_id] = next_node
                else:
                    prev_node = cur_node.previous
                    next_node = cur_node.next

                    prev_node.next = next_node
                    if next_node is not None:
                        next_node.previous = prev_node

            cur_node = cur_node.next

    def check(self, i: int) -> List[str]:
        result = []
        if self.table[i] is None:
            return result
        cur_node = self.table[i]
        while cur_node:
            result.append(cur_node.value)
            cur_node = cur_node.next
        return result


def main():
    m = int(input())
    table = Table(m)

    n = int(input())
    for _ in range(n):
        commands = input().split()

        if commands[0] == 'add':
            string = commands[1]
            table.add(string)

        elif commands[0] == 'del':
            string = commands[1]
            table.delete_key(string)

        elif commands[0] == 'check':
            index = int(commands[1])
            arr = table.check(index)
            print(' '.join(arr))

        elif commands[0] == 'find':
            string = commands[1]
            result = table.find(string)
            result = 'yes' if result else 'no'
            print(result)


if __name__ == '__main__':
    main()

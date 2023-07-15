class Stack:

    def __init__(self):
        self._stack = []
        self._max_stack = []

    def pop(self):
        if self._stack:
            elem = self._stack.pop()
            self._max_stack.pop()
            return elem

    def push(self, elem):
        if self._stack:
            new_max = max(elem, self._max_stack[-1])
            self._stack.append(elem)
            self._max_stack.append(new_max)
        else:
            self._stack.append(elem)
            self._max_stack.append(elem)

    def get_max(self):
        if self._max_stack:
            return self._max_stack[-1]


def main():
    n = int(input())
    stack = Stack()
    for _ in range(n):
        commands = input().split()
        if commands[0] == 'push':
            elem = int(commands[1])
            stack.push(elem)
        elif commands[0] == 'pop':
            stack.pop()
        else:
            max_elem = stack.get_max()
            print(max_elem)


if __name__ == '__main__':
    main()

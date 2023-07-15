def check_brackets(s: str) -> str:
    open_brackets = {'(', '[', '{'}
    close_brackets = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    stack = []
    indices = []
    for i, symbol in enumerate(s):
        if symbol in open_brackets:
            stack.append(symbol)
            indices.append(i)

        elif symbol in close_brackets.keys():
            if len(stack) > 0 and close_brackets[symbol] == stack[-1]:
                del stack[-1]
                del indices[-1]
            else:
                return str(i + 1)

    return 'Success' if len(stack) == 0 else (indices[-1] + 1)


def main():
    s = input()
    result = check_brackets(s)
    print(result)


if __name__ == '__main__':
    main()

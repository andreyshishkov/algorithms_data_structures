def main():
    book = {}
    n = int(input())
    for _ in range(n):
        commands = input().split()
        if commands[0] == 'add':
            number = commands[1]
            name = commands[2]
            book[number] = name

        elif commands[0] == 'del':
            number = commands[1]
            if number in book.keys():
                del book[number]

        else:
            number = commands[1]
            name = book.get(number, 'not found')
            print(name)


if __name__ == '__main__':
    main()

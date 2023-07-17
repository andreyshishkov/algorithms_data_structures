from typing import List


def get_hash(string: str, p: int, x: int):
    value = 0
    for i, char in enumerate(string):
        value += ord(char) * pow(x, i, p)
    k = len(string) - 1
    value %= p
    return value, ord(string[-1]) * pow(x, k) % p


def find_pattern(pattern: str, text: str, p, x) -> List[int]:
    len_text = len(text)
    len_pattern = len(pattern)

    pattern_key = get_hash(pattern, p, x)[0]

    win_prev = text[-len_pattern:]
    win_prev_key, monom_prev = get_hash(win_prev, p, x)

    answer = []
    pow_p = pow(x, len_pattern - 1) % p
    for i in range(-2, -(len_text - len_pattern) - 2, -1):
        if win_prev_key == pattern_key:
            answer.append(len_text + i - len_pattern + 2)

        win_prev_key = ((win_prev_key - monom_prev) * x + ord(text[i - len_pattern + 1])) % p
        win_prev_key = (win_prev_key + p) % p
        monom_prev = (ord(text[i]) * pow_p) % p

    if win_prev_key == pattern_key:
        answer.append(0)

    return answer[::-1]


def main():
    pattern = input()
    text = input()

    x = 29
    p = 999_999_000_001
    result = find_pattern(pattern, text, p, x)
    print(*result)


if __name__ == '__main__':
    main()

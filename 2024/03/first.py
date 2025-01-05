import re
import math

def apply_mult(input):
    print(input)
    pattern = re.compile(r"\d{1,3}")
    res = re.findall(pattern, input)
    print(res)
    res = [int(x) for x in res]
    return math.prod(res)


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    res = re.findall(pattern, raw)

    s = sum([apply_mult(x) for x in res])
    print(s)


if __name__ == '__main__':
    main()
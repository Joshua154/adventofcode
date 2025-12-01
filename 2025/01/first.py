def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    start = 50
    hit_zero = 0

    for line in raw:
        pre = start
        dir, val = line[0], int(line[1:])
        if dir == "R":
            start += val
        elif dir == "L":
            start -= val

        start %= 100

        print("move from", pre, "to", start)

        if start == 0:
            hit_zero += 1

    print(hit_zero)


if __name__ == '__main__':
    main()
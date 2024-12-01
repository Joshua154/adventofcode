

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    f, l = [], []

    for line in raw:
        s = line.split("   ")
        f.append(s[0])
        l.append(s[1])


    f, l = sorted(f), sorted(l)

    print(sum(list(map(lambda x,y: abs(int(x) - int(y)), f, l))))


if __name__ == '__main__':
    main()
def to_int(numbers: list):
    n = []
    for number in numbers:
        number = int(number)
        n.append(number)
    return n

def to_dict(numbers) -> dict:
    dictionary = {}
    for i in list(dict.fromkeys(numbers)):
        dictionary[i] = numbers.count(i)
    return dictionary


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    f, l = [], []

    for line in raw:
        s = line.split("   ")
        f.append(s[0])
        l.append(s[1])


    f, l = to_int(sorted(f)), to_int(sorted(l))

    l = to_dict(l)
    print(sum(map(lambda x: x * l[x] if x in l else 0, f)))


if __name__ == '__main__':
    main()
def getDiff(a, b):
    return a - b

def parseData(raw):
    data = []
    for line in raw:
        data.append(line.split(" "))
    data = [[int(x) for x in y] for y in data]
    return data

def parseDiff(data):
    diff = []
    for i in range(1, len(data)):
        diff.append(getDiff(int(data[i]), int(data[i-1])))
    if len(diff) == 0:
        diff.append(0)
    return diff

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")
    raw = [x for x in raw if x != ""]

    parsed = []
    data = parseData(raw)

    for d in data:
        parsed.append([])
        currentDiffs = d
        parsed[-1].append(currentDiffs)
        while set(currentDiffs) != {0}:
            currentDiffs = parseDiff(currentDiffs)
            parsed[-1].append(currentDiffs)


    result = 0
    for line in parsed:
        line = line[::-1]
        r = 0
        for i in range(len(line)):
            if(i == 0):
                o = line[i][::-1]
                o.append(0)
                line[i] = o[::-1]
            else:
                o = line[i][::-1]
                o.append(o[-1] - line[i-1][0])
                line[i] = o[::-1]
                r = line[i][0]

        result += r

    for i in parsed:
        print(i)
    print(result)


if __name__ == "__main__":
    main()

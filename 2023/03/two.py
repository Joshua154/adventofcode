def getNumberList(data):
    symbolList = []
    for i in range(len(data)):
        symbolList.append([])
        for j in range(len(data[i])):
            elm = data[i][j]
            if not elm == "." and elm.isnumeric():
                symbolList[-1].append(j)
    return symbolList


def searchForGears(data, sur):
    gears = []
    for x, y in sur:
        if (data[x][y] == "*"):
            gears.append([x, y])
    return gears


def parseNumbers(numberList, data):
    numbers = []
    for y in range(len(numberList)):
        if len(numberList[y]) == 0:
            continue

        xMin = numberList[y][0]
        xMax = numberList[y][0]

        for x in range(1, len(numberList[y])):
            if numberList[y][x] - xMax == 1:
                xMax = numberList[y][x]
            else:
                numbers.append({
                    "xMin": xMin,
                    "xMax": xMax,
                    "number": "".join([str(i) for i in data[y][xMin:xMax + 1]]),
                    "row": y,
                })
                xMin = numberList[y][x]
                xMax = numberList[y][x]

        numbers.append({
            "xMin": xMin,
            "xMax": xMax,
            "number": "".join([str(i) for i in data[y][xMin:xMax + 1]]),
            "row": y,
        })

    return numbers


def getSourroundings(data, row, xMin, xMax):
    surroundings = []
    for y in range(-1, 2):
        if row + y < 0 or row + y > len(data) - 1:
            continue
        minV = max(xMin - 1, 0)
        maxV = min(xMax + 2, len(data[row + y]))
        for x in range(minV, maxV):
            surroundings.append([row + y, x])
    return surroundings


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    parse_numbers = parseNumbers(getNumberList(raw), raw)
    gears = []
    numbers = []

    for i in parse_numbers:
        sur = getSourroundings(raw, i["row"], i["xMin"], i["xMax"])
        gears.append(searchForGears(raw, sur))

        numbers.append({
            "number": i["number"],
            "sur": sur
        })

    result = []
    for i in range(len(gears)):
        elm = gears[i]
        if gears.count(elm) == 2:
            for j in range(len(gears)):
                if i == j:
                    continue
                if gears[i] == -1 or gears[j] == -1:
                    continue
                if gears[i] == gears[j]:
                    result.append(int(numbers[i]["number"]) * int(numbers[j]["number"]))
                    gears[j] = -1
                    gears[i] = -1

    print(sum(result))

if __name__ == "__main__":
    main()

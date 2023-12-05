def getNumberList(data):
    symbolList = []
    for i in range(len(data)):
        symbolList.append([])
        for j in range(len(data[i])):
            elm = data[i][j]
            if not elm == "." and elm.isnumeric():
                symbolList[-1].append(j)
    return symbolList


def getSurroundingSymbols(data, row, xMin, xMax):
    surroundings = []
    for y in range(-1, 2):
        if row + y < 0 or row + y > len(data) - 1:
            continue
        print(data[row + y][max(xMin - 1, 0):min(xMax + 2, len(data[row + y]))])
        for x in range(xMin - 1, xMax + 2):
            if x < 0 or x > len(data[row + y]) - 1:
                continue

            if y == 0 and xMin <= x <= xMax:
                continue

            if not data[row + y][x] == "." and not data[row + y][x].isnumeric():
                surroundings.append(data[row + y][x])
    return surroundings


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


def main():
    with open("./message.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    parse_numbers = parseNumbers(getNumberList(raw), raw)

    symbol_numbers = []
    symbol_numbers2 = []
    for i in parse_numbers:
        sour = getSurroundingSymbols(raw, i["row"], i["xMin"], i["xMax"])
        print(i, sour)
        print("\n")
        if (len(sour) > 0):
            symbol_numbers.append(int(i["number"]))
    #         symbol_numbers2.append(i)
    #
    # symbol_numbers2.sort(key=lambda x: int(x["number"]))
    # with open("./output.txt", "w", encoding="utf-8") as f:
    #     for i in symbol_numbers2:
    #         f.write(str(i["number"]) + ", y:" + str(i["row"]) + " x:" + str(i["xMin"]) + "-" + str(i["xMax"]) + "\n")

    print(sum(symbol_numbers))


if __name__ == "__main__":
    main()

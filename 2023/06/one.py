def parseData(raw):
    data = {}
    raw = raw.split("\n\n")
    raw = [i.split("\n") for i in raw]
    raw = [[j.split(": ") for j in i] for i in raw]

    seeds = [int(i) for i in raw.pop(0)[0][1].split(" ")]

    for i in raw:
        mapName = "".join(i[0]).replace(":", "").replace(" map", "")
        data[mapName] = []
        for j in i[1:]:
            for k in j:
                if (k == ''):
                    continue

                data[mapName].append([int(num) for num in k.split(" ")])
    print(data)
    return seeds, data


def getPosition(startIndex, num):
    return num - startIndex


def isInRange(startIndex, range, num):
    return startIndex <= num <= startIndex + range - 1


def getDestination(mapName, data, num):
    for mapData in data[mapName]:
        if isInRange(mapData[1], mapData[2], num):
            return mapData[0] + getPosition(mapData[1], num)
    return num


def parseSeeds(seeds, data):
    mapNames = list(data.keys())

    seedMap = {}

    for seed in seeds:
        seedMap[seed] = {}
        dest = seed
        for mapName in mapNames:
            dest = getDestination(mapName, data, dest)
            seedMap[seed][mapName] = dest
    return seedMap


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    seeds, data = parseData(raw)
    seedMap = parseSeeds(seeds, data)

    locations = []
    for seed in seedMap:
        locations.append(seedMap[seed]["humidity-to-location"])

    print(min(locations))


if __name__ == "__main__":
    main()

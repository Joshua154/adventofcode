from datetime import datetime

from one import parseData, parseSeeds


def main():
    start = datetime.now()
    print("start at: " + str(datetime.now()))
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    tempSeeds, data = parseData(raw)

    best = {}
    for i in range(0, len(tempSeeds), 2):
        for j in range(tempSeeds[i], tempSeeds[i] + tempSeeds[i + 1]):
            seedMap = parseSeeds([j], data)

            if best == {}:
                best = seedMap[j]
            elif best["humidity-to-location"] > seedMap[j]["humidity-to-location"]:
                best = seedMap[j]

    print(best)
    print("end at: " + str(datetime.now()))
    print("time taken: " + str(datetime.now() - start))


if __name__ == "__main__":
    main()

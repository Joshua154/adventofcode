import threading
from datetime import datetime

from one import parseData, parseSeeds

def threadFunction(data, seed, best):
    seedMap = parseSeeds([seed], data)

    if best == []:
        best.append(seedMap[seed])
    elif best[0]["humidity-to-location"] > seedMap[seed]["humidity-to-location"]:
        best[0] = seedMap[seed]

def main():
    start = datetime.now()
    threads = []
    print("start at: " + str(datetime.now()))
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    tempSeeds, data = parseData(raw)

    best = []
    for i in range(0, len(tempSeeds), 2):
        for j in range(tempSeeds[i], tempSeeds[i] + tempSeeds[i + 1]):
            while len(threads) >= 50000:
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)

            iThread = threading.Thread(target=threadFunction, args=(data, j, best))
            iThread.start()
            threads.append(iThread)


    print(best)
    print("end at: " + str(datetime.now()))
    print("time taken: " + str(datetime.now() - start))


if __name__ == "__main__":
    main()

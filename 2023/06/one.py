def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    times, distance, _ = raw.split("\n")
    _, times = times.split(":")
    _, distance = distance.split(":")

    times = times.split(" ")
    distance = distance.split(" ")

    times = [int(i) for i in filter(lambda x: x != "", times)]
    distance = [int(i) for i in filter(lambda x: x != "", distance)]

    difWays = {}
    for i in range(len(times)):
        best = distance[i]
        difWays[i] = 0
        for j in range(times[i] + 1):
            speed = j
            d = speed * (times[i] - j)
            if(d > best):
                difWays[i] += 1

    res = 1
    for i in range(len(times)):
        res *= difWays[i]

    print(res)





if __name__ == "__main__":
    main()

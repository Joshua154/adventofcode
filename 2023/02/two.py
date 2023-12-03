from one import parseGames

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    data = parseGames(raw)
    pows = []
    for game, maxCubes in data.items():
        pow = 1
        for color, maxCube in maxCubes.items():
            pow *= maxCube
        pows.append(pow)

    print(sum(pows))

if __name__ == "__main__":
    main()

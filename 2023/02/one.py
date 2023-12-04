def parseGames(raw):
    result = {}

    for row in raw:
        if row == "":
            continue
        maxCubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }

        game, data = row.split(": ")
        game = int(game.replace("Game ", ""))

        for round in data.split("; "):
            for cube in round.split(", "):
                count, color = cube.split(" ")
                count = int(count)

                if count > maxCubes[color]:
                    maxCubes[color] = count

        result[game] = maxCubes
    return result

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    maxCubesInput = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    result = parseGames(raw)

    games = []

    for game, maxCubes in result.items():
        isBigger = False
        for color, maxCube in maxCubes.items():
            if maxCube > maxCubesInput[color]:
                isBigger = True
                break
        if not isBigger:
            games.append(game)


    print(sum(games))

if __name__ == "__main__":
    main()


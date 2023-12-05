def parseCard(row):
    if row == "":
        return
    cardId, nums = row.split(":")
    cardId = int(cardId.replace("Card ", ""))

    nums = nums.replace("  ", " 0")

    winNums, nums = nums.split("|")

    winNums = winNums.split(" ")
    finalWinNums = []
    for i in range(len(winNums)):
        if winNums[i] == "":
            continue
        finalWinNums.append(int(winNums[i]))

    nums = nums.split(" ")
    finalNums = []
    for i in range(len(nums)):
        if nums[i] == "":
            continue
        finalNums.append(int(nums[i]))

    return {
        "id": cardId,
        "winNum": finalWinNums,
        "num": finalNums,
    }


def getInter(card):
    return [x for x in card["winNum"] if x in card["num"]]


def calcScore(card):
    score = 0
    for i in getInter(card):
        if score == 0:
            score = 1
        else:
            score *= 2
    return score


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    cards = []
    for i in range(len(raw)):
        card = parseCard(raw[i])
        if card is None:
            continue
        cards.append(card)

    for i in range(len(cards)):
        cards[i]["score"] = calcScore(cards[i])
        print(cards[i])

    print(sum([card["score"] for card in cards]))


if __name__ == "__main__":
    main()

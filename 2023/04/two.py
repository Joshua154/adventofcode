from one import calcScore
from one import parseCard
from one import getInter


def winAmount(card):
    return len(card["inter"])


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
        cards[i]["inter"] = getInter(cards[i])
        cards[i]["amount"] = 1
        cards[i]["dub"] = [(x + cards[i]["id"] + 1) for x in range(winAmount(cards[i]))]
        # cards[i]["orgdub"] = cards[i]["dub"]

        print(cards[i])

    cardAmounts = {}

    for card in cards:
        cardAmounts[card["id"]] = 1
    for card in cards:
        for j in range(card["amount"]):
            for i in card["dub"]:
                cardAmounts[i] += 1
                cards[i - 1]["amount"] += 1

    print(cardAmounts)
    total = max(cardAmounts.values())
    print(total)

if __name__ == "__main__":
    main()

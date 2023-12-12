l = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
h = ["FiK", "FoK", "FH", "TK", "TP", "OP", "HC"]


class Card:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return l.index(self.value) > l.index(other.value)

    def getValue(self):
        return len(l) - l.index(self.value)

    def compare(self, other):
        if self.value == other.value:
            return 0
        elif self.value > other.value:
            return 1
        else:
            return -1


class Hand:
    def __init__(self, cards, bid):
        if (len(cards) != 5):
            raise Exception("Hand must have 5 cards")
        self.cards = cards
        self.bid = bid
        self.type = self.get_type()

    def __gt__(self, other):
        if h.index(self.type) != h.index(other.type):
            return h.index(self.type) > h.index(other.type)
        else:
            for i in range(len(self.cards)):
                if self.cards[i].compare(other.cards[i]) != 0:
                    return self.cards[i] > other.cards[i]
            return False

    def __str__(self):
        return str([l[len(l) - x.getValue()] for x in self.cards]) + ", " + str(self.bid) + ", " + self.type

    def get_type(self):
        # c = list(map(lambda x: x.getValue(), self.cards))
        # for i in list(set(c)):
        #     print(i, c.count(i))

        if self.isFiveOfKind():
            return "FiK"
        elif self.isFourOfKind():
            return "FoK"
        elif self.isFullHouse():
            return "FH"
        elif self.isThreeOfKind():
            return "TK"
        elif self.isTwoPair():
            return "TP"
        elif self.isOnePair():
            return "OP"
        else:
            return "HC"

    def isFiveOfKind(self):
        c = list(map(lambda x: x.getValue(), self.cards))
        for i in list(set(c)):
            if c.count(i) == 5:
                return True
        return False

    def isFourOfKind(self):
        c = list(map(lambda x: x.getValue(), self.cards))
        for i in list(set(c)):
            if c.count(i) == 4:
                return True
        return False

    def isFullHouse(self):
        return self.isThreeOfKind() and self.isOnePair()

    def isThreeOfKind(self):
        c = list(map(lambda x: x.getValue(), self.cards))
        for i in list(set(c)):
            if c.count(i) == 3:
                return True
        return False

    def isTwoPair(self):
        count = 0
        c = list(map(lambda x: x.getValue(), self.cards))
        for i in list(set(c)):
            if c.count(i) == 2:
                count += 1
        return count == 2

    def isOnePair(self):
        c = list(map(lambda x: x.getValue(), self.cards))
        for i in list(set(c)):
            if c.count(i) == 2:
                return True
        return False


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    hands, bids = [], []
    for i in raw:
        if(i == ""):
            continue
        hands.append(i.split(" ")[0])
        bids.append(i.split(" ")[1])

    for i in range(len(hands)):
        cards = []
        for j in range(len(hands[i])):
            cards.append(Card(hands[i][j]))
        hands[i] = Hand(cards, int(bids[i]))

    hands = sorted(hands)

    sum = 0
    for i in range(len(hands)):
        sum += (len(hands) - i) * hands[i].bid
        print(hands[i])

    print(sum)


if __name__ == "__main__":
    main()

l = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
h = ["FiK", "FoK", "FH", "TK", "TP", "OP", "HC"]


class Card:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return l.index(self.value) > l.index(other.value)

    def getValue(self):
        return len(l) - l.index(self.value)

    def compare(self, other):
        if self.getValue() == other.getValue():
            return 0
        elif self.getValue() > other.getValue():
            return 1
        else:
            return -1


class Hand:
    def __init__(self, cards, bid, findBest=True):
        if (len(cards) != 5):
            raise Exception("Hand must have 5 cards")
        self.cards = cards
        self.bid = bid
        self.type = self.get_type()
        if findBest:
            self.findBest()

    def __gt__(self, other):
        if h.index(self.type) != h.index(other.type):
            return h.index(self.type) > h.index(other.type)
        else:
            for i in range(len(self.cards)):
                print(self.cards[i].value, other.cards[i].value)
                if self.cards[i].compare(other.cards[i]) != 0:
                    return self.cards[i] > other.cards[i]
            return False

    def __str__(self):
        return str([l[len(l) - x.getValue()] for x in self.cards]) + ", " + str(self.bid) + ", " + self.type

    def findBest(self):
        # best = self.get_type()
        # cards = self.cards
        # for i in range(5):
        #     tempCards = self.cards
        #     for a in l:
        #         if cards[i].value == "J":
        #             self.cards[0] = Card(a)
        #     if self.get_type() > best:
        #         best = self.get_type()
        #         cards = self.cards
        #     self.cards = tempCards
        #
        # self.cards = cards
        # self.type = best

        # best = self.get_type()
        # cards = self.cards.copy()
        # cards_ = list(set([y.value for y in self.cards]))
        # for first in cards_:
        #     for second in cards_:
        #         for third in cards_:
        #             for fourth in cards_:
        #                 for fifth in cards_:
        #                     tempCards = self.cards.copy()
        #                     if self.cards[0].value == "J":
        #                         self.cards[0].value = first
        #                     if self.cards[1].value == "J":
        #                         self.cards[1].value = second
        #                     if self.cards[2].value == "J":
        #                         self.cards[2].value = third
        #                     if self.cards[3].value == "J":
        #                         self.cards[3].value = fourth
        #                     if self.cards[4].value == "J":
        #                         self.cards[4].value = fifth
        #
        #                     print(best, self.get_type())
        #
        #                     if self.get_type() > best:
        #                         print("New best:", best, cards)
        #                         best = self.get_type()
        #                         cards = self.cards.copy()
        #                     self.cards = tempCards
        #
        # self.cards = cards
        # self.type = best##

        if("J" not in [x.value for x in self.cards]):
            return

        print("\n")
        print([str(x.value) for x in self.cards])
        best = self.get_type()
        cards = self.cards.copy()
        cards_ = list(set([y.value for y in self.cards]))
        for first in cards_:
            for second in cards_:
                for third in cards_:
                    for fourth in cards_:
                        for fifth in cards_:
                            tempCards = self.cards.copy()
                            if self.cards[0].value == "J":
                                self.cards[0].value = first
                            if self.cards[1].value == "J":
                                self.cards[1].value = second
                            if self.cards[2].value == "J":
                                self.cards[2].value = third
                            if self.cards[3].value == "J":
                                self.cards[3].value = fourth
                            if self.cards[4].value == "J":
                                self.cards[4].value = fifth

                            print([str(x.value) for x in self.cards])
                            if h.index(self.get_type()) > h.index(best):
                                best = self.get_type()
                                cards = self.cards.copy()
                            self.cards = tempCards
        self.cards = cards
        self.type = self.get_type()


    def get_type(self):
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
    with open("./testInput.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")

    hands, bids = [], []
    for i in raw:
        if (i == ""):
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

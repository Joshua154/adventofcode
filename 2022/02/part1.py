with open("./2022/02/input.txt", "r", encoding="utf-8") as f:
    raw = f.read().split("\n")

list = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

numList = {
    "A": 1,
    "B": 2,
    "C": 3
}

rounds = []
for elm in raw:
    elm = elm.split(" ")
    rounds.append(0)

    if(elm[0] == list.get(elm[1])):
        rounds[-1] += 3 + numList.get(elm[0])
    elif((elm[0] == "A" and list.get(elm[1]) == "c") or (elm[0] == "B" and list.get(elm[1]) == "a") or (elm[0] == "C" and list.get(elm[1]) == "b")):
        rounds[-1] += 6

    rounds[-1] += numList.get(elm[0])

print(sum(rounds))
def getNode(line):
    name, links = line.split("=")
    links = links.replace("(", "").replace(")", "").split(",")
    name, links = name.strip(), [l.strip() for l in links]
    return name, links


def getFirstLastNode(raw):
    return getNode(raw[0])[0], getNode(raw[-1])[0]


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    raw = raw.split("\n")
    dir, raw = raw[0], raw[1::]
    raw = [r for r in raw if r != ""]

    nodes = {}

    for line in raw:
        if (line == ""):
            continue
        name, n = getNode(line)
        nodes[name] = n

    dirPointer = 0
    step = 0

    print(raw)
    node = "AAA"
    lastNode = "ZZZ"

    while node != lastNode:
        curDir = dir[dirPointer]
        if curDir == "L":
            node = nodes[node][0]
        else:
            node = nodes[node][1]
        dirPointer = (dirPointer + 1) % len(dir)
        step += 1
        print(step, dirPointer, node, lastNode)

    print(step)


if __name__ == "__main__":
    main()

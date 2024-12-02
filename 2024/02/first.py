def get_dif(input, i):
    if i == len(input) - 1: return
    diff = input[i+1] - input[i]
    if abs(diff) > 3 or abs(diff) < 1:
        return 0
    return 1 if diff > 0 else -1

def get_res(row):
    res = None
    for j in range(len(row) - 1):
        dif = get_dif(row, j)
        if res == None:
            res = dif

        if res != dif:
            return False
    return True

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    raw = raw[:-1]
    for i in range(len(raw)):
        raw[i] = raw[i].split(" ")
        raw[i] = [int(x) for x in raw[i]]
        raw[i] = get_res(raw[i])

    print(raw.count(True))






if __name__ == '__main__':
    main()
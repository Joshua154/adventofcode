def overwriteNums(raw):
    returnArr = []
    numDict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    for j in range(len(raw)):
        row = raw[j]
        for i in range(-6, len(row)):
            sub = row[max(0, i):min(i + 6, len(row))]
            for key in numDict:
                if key in sub:
                    row = row.replace(key, str(numDict[key]))

        # i = 0
        # foundDigit = False
        # while i < len(row) and not foundDigit:
        #     if row[max(0, i - 1)].isnumeric():
        #         foundDigit = True
        #         break
        #     sub = row[:i]
        #     print(j, "->", row, sub)
        #     for key in numDict:
        #         if key in sub:
        #             row = row.replace(key, str(numDict[key]), 1)
        #             print("found", key)
        #             foundDigit = True
        #             break
        #     i += 1
        #
        # i = len(row) - 1
        # foundDigit = False
        # while i > 0 and not foundDigit:
        #     if row[min(len(row) - 1, i + 1)].isnumeric():
        #         foundDigit = True
        #         break
        #     sub = row[i:]
        #     print(j, "<-", row, sub)
        #     for key in numDict:
        #         if key in sub:
        #             row = row.replace(key, str(numDict[key]))
        #             print("found", key)
        #             foundDigit = True
        #             break
        #     i -= 1

        returnArr.append(row)
    return returnArr


def getFistAndLast(raw):
    results = []
    for i in raw:
        nums = []
        for j in i:
            if j.isnumeric():
                nums.append(j)
        results.append(10 * int(nums[0]) + int(nums[-1]))
    return results


def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    data = overwriteNums(raw)
    firstAndLast = getFistAndLast(data)
    print(sum(firstAndLast))


if __name__ == "__main__":
    main()

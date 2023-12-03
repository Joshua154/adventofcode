def getCalcs(raw):
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
    print(sum(getCalcs(raw)))


if __name__ == "__main__":
    main()


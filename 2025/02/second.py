def isInvalid(num):
    num = str(num)

    if num.startswith("0"):
        return True
    if len(num) < 2:
        return False

    n = len(num)
    for size in range(1, n // 2 + 1):
        if n % size != 0:
            continue
        if num[:size] * (n // size) == num:
            return True
    return False

def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    line = "".join(raw)

    ranges = line.split(",")
    ranges = [r.split("-") for r in ranges]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]

    invalid_sum = 0

    for (start, end) in ranges:
        for num in range(start, end + 1):
            if isInvalid(num):
                invalid_sum += num
        

    print(invalid_sum)
    
if __name__ == '__main__':
    main()
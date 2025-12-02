def isInvalid(num):
    num = str(num)

    if num.startswith("0"):
        return True
    
    if len(num) % 2 != 0:
        return False
    
    length = len(num)//2
    return num[:length] == num[length:]

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
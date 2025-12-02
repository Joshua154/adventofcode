
def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    raw = raw.split("\n")
    
    start = 50
    at_zero = 0
    crosses = 0

    directions = [(-1 if line[0] == 'L' else 1) * int(line[1:]) for line in raw]

    for steps in directions:
        (multiple, remainder) = divmod(start + steps, 100)

        if multiple < 0 and start == 0:
            multiple += 1

        if multiple > 0 and remainder == 0:
            multiple -= 1
            
        at_zero += 1 if remainder == 0 else 0
        crosses += abs(multiple)
        start = remainder

    print(at_zero + crosses)


if __name__ == '__main__':
    main()
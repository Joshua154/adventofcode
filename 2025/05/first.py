def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    chunks = raw.split('\n\n')
    ranges = chunks[0].split('\n')
    numbers = chunks[1].split('\n')

    numbers = [int(n) for n in numbers if n]
    ranges = [(int(start), int(end)) for start, end in (r.split('-') for r in ranges)]

    count = 0
    for number in numbers:
        for (start, end) in ranges:
            if start <= number <= end:
                count += 1
                break
    print(count)


if __name__ == '__main__':
    main()
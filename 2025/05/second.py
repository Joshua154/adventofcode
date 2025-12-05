def main():
    with open("./input.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    chunks = raw.split('\n\n')
    ranges = chunks[0].split('\n')
    
    ranges = [(int(start), int(end)) for start, end in (r.split('-') for r in ranges)]

    cur_ranges = []
    for cur_start, cur_end in ranges:
        new_ranges = []
        while cur_ranges:
            start, end = cur_ranges.pop()

            overlap_start = max(cur_start, start)
            overlap_end = min(cur_end, end)

            overlap_diff = overlap_end - overlap_start + 1

            if overlap_diff < 0:
                new_ranges.append((start, end))
            else:
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)

        new_ranges.append((cur_start, cur_end))
        cur_ranges = new_ranges

    print(sum([end - start + 1 for start, end, in cur_ranges]))


if __name__ == '__main__':
    main()
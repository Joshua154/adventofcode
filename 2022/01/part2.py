with open("./2022/01/input.txt", "r", encoding="utf-8") as f:
    raw = f.read()

raw = raw.split("\n\n")
for elv in raw:
    raw[raw.index(elv)] = elv.split("\n")

elves = []

for elv in raw:
    elves.append(0)
    for fruit in elv:
        elves[-1] += int(fruit)

out = 0
for i in range(3):
    out += max(elves)
    elves.pop(elves.index(max(elves)))

print(out)
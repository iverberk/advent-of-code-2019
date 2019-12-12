import re
import operator

moons = []

with open('input') as f:
    for position in f:
        moons.append({
            'p': list(map(int, re.findall(r"(-?\d+)", position))),
            'v': [0, 0, 0]
        })

for step in range(0, 1000):
    for moon, m1 in enumerate(moons):
        for m2 in moons:

            if m1['p'] == m2['p']:
                continue

            x1, y1, z1 = m1['p']
            x2, y2, z2 = m2['p']

            if x1 != x2:
                m1['v'][0] += -1 if x1 > x2 else 1

            if y1 != y2:
                m1['v'][1] += -1 if y1 > y2 else 1

            if z1 != z2:
                m1['v'][2] += -1 if z1 > z2 else 1

        moons[moon] = m1

    for index, moon in enumerate(moons):
        moons[index]['p'] = list(map(operator.add, moon['p'], moon['v']))

print(sum(sum(map(abs, moon['p'])) * sum(map(abs, moon['v'])) for moon in moons))

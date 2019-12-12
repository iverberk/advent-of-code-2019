import re
import operator
from itertools import count
from math import gcd

moons = []
initial_state_x, initial_state_y, initial_state_z = [], [], []
state_x, state_y, state_z = [], [], []
cycle_x, cycle_y, cycle_z = False, False, False

with open('input') as f:
    for position in f:
        x, y, z = list(map(int, re.findall(r"(-?\d+)", position)))
        moons.append({
            'p': [x, y, z],
            'v': [0, 0, 0]
        })

        initial_state_x.append(x)
        initial_state_y.append(y)
        initial_state_z.append(z)

state_x = initial_state_x.copy()
state_y = initial_state_y.copy()
state_z = initial_state_z.copy()

for step in count(2):

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
        x, y, z = list(map(operator.add, moon['p'], moon['v']))

        state_x[index] = x
        state_y[index] = y
        state_z[index] = z

        moons[index]['p'] = (x, y, z)

    if state_x == initial_state_x:
        if not cycle_x:
            cycle_x = step

    if state_y == initial_state_y:
        if not cycle_y:
            cycle_y = step

    if state_z == initial_state_z:
        if not cycle_z:
            cycle_z = step

    if cycle_x and cycle_y and cycle_z:
        break


def lcm(a, b):
    return int(a * b / gcd(a, b))


print(lcm(lcm(cycle_x, cycle_y), cycle_z))

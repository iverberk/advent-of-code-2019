import math

astroids = []

with open('input') as f:
    for y, line in enumerate(f):
        for x, loc in enumerate(line.strip()):
            if loc == '#':
                astroids.append((x, y))

max_targets = 0
station = None
for astroid in astroids:
    x, y = astroid
    targets = {}

    for target in astroids:
        if astroid == target:
            continue

        tx, ty = target
        dx, dy = tx - x, ty - y

        degrees = 90 + math.degrees(math.atan2(dy, dx))
        if degrees < 0:
            degrees += 360

        targets[degrees] = target

    if len(targets) > max_targets:
        station = {'position': astroid, 'targets': targets}
        max_targets = len(targets)

print(station['position'], len(station['targets']))

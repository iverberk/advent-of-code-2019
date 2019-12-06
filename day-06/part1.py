with open('input') as f:

    orbits, orbit_map = 0, {}

    for orbit in f:
        objs = orbit.strip().split(')')
        orbit_map[objs[1]] = objs[0]

    for obj in orbit_map.keys():
        while obj != 'COM':
            orbits += 1
            obj = orbit_map[obj]

print(orbits)

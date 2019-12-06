with open('input') as f:

    orbit_map = {}
    for orbit in f:
        objs = orbit.strip().split(')')
        orbit_map[objs[1]] = objs[0]

    # Calculate YOU orbits
    obj = orbit_map['YOU']
    you_orbits = [obj]
    while obj != 'COM':
        you_orbits.append(orbit_map[obj])
        obj = orbit_map[obj]

    # Calculate SAN orbits
    obj = orbit_map['SAN']
    san_orbits = [obj]
    while obj != 'COM':
        san_orbits.append(orbit_map[obj])
        obj = orbit_map[obj]

    # Find the common orbits
    cos = set(you_orbits).intersection(san_orbits)

# Calculate minimal length of common orbits
print(min([you_orbits.index(co) + san_orbits.index(co) for co in cos]))

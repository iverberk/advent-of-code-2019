from collections import defaultdict, deque
from intcode import Intcode

area = defaultdict(lambda: '.')
NORTH, SOUTH, EAST, WEST = 1, 2, 3, 4

area[(0, 0)] = 'S'
tiles = {0: '#', 1: '.', 2: 'O'}

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)

    def move(self, direction):
        # print(f"Moving in {direction} direction")

        if direction == NORTH:
            intcode.send(NORTH)
            status = intcode.receive()
            if status:
                self.y -= 1

        if direction == SOUTH:
            intcode.send(SOUTH)
            status = intcode.receive()
            if status:
                self.y += 1

        if direction == WEST:
            intcode.send(WEST)
            status = intcode.receive()
            if status:
                self.x += 1

        if direction == EAST:
            intcode.send(EAST)
            status = intcode.receive()
            if status:
                self.x -= 1

        if status == 2:
            area[(self.x, self.y)] = tiles[status]
            print("Oxygen location: ", self.x, self.y)
            return True

        return False

    def get_neighbours(self):

        neighbours = []

        # Try NORTH
        intcode.send(NORTH)
        status = intcode.receive()
        if status:
            neighbours.append((self.x, self.y - 1, NORTH))

            # Move back
            intcode.send(SOUTH)
            _ = intcode.receive()
        else:
            area[(self.x, self.y - 1)] = tiles[status]

        # Try SOUTH
        intcode.send(SOUTH)
        status = intcode.receive()
        if status:
            neighbours.append((self.x, self.y + 1, SOUTH))

            # Move back
            intcode.send(NORTH)
            _ = intcode.receive()
        else:
            area[(self.x, self.y + 1)] = tiles[status]

        # Try WEST
        intcode.send(WEST)
        status = intcode.receive()
        if status:
            neighbours.append((self.x + 1, self.y, WEST))

            # Move back
            intcode.send(EAST)
            _ = intcode.receive()
        else:
            area[(self.x + 1, self.y)] = tiles[status]

        # Try EAST
        intcode.send(EAST)
        status = intcode.receive()
        if status:
            neighbours.append((self.x - 1, self.y, EAST))

            # Move back
            intcode.send(WEST)
            _ = intcode.receive()
        else:
            area[(self.x - 1, self.y)] = tiles[status]

        return neighbours

    def take_path(self, path, reverse=False):

        for index, step in enumerate(path):
            _, _, direction = step

            if not direction:
                continue

            if reverse:
                direction = self._reverse_direction(direction)

            oxygen_found = self.move(direction)
            if oxygen_found:
                print(index)

    def _reverse_direction(self, direction):
        if direction == NORTH:
            return SOUTH
        elif direction == SOUTH:
            return NORTH
        elif direction == EAST:
            return WEST
        elif direction == WEST:
            return EAST


def print_area():
    if not area:
        return
    minx = min([k[0] for k in area.keys()])
    maxx = max([k[0] for k in area.keys()])
    miny = min([k[1] for k in area.keys()])
    maxy = max([k[1] for k in area.keys()])

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(area[(x, y)], end='')
        print('')


memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

intcode = Intcode(memory)

robot = Robot(0, 0)
seen, queue = set([(0, 0)]), deque([[(0, 0, 0)]])

# Find the oxygen and build the map
while queue:
    path = queue.popleft()

    robot.take_path(path)
    neighbours = robot.get_neighbours()

    for neighbour in neighbours:
        x, y, direction = neighbour
        if (x, y) not in seen:
            seen.add((x, y))

            new_path = list(path)
            new_path.append((x, y, direction))

            queue.append(new_path)

    path.reverse()
    robot.take_path(path, reverse=True)

oxygen = None
for location, status in area.items():
    if status == 'O':
        oxygen = location

print(oxygen)


def nb(pos):
    x, y = pos
    neighbours = []
    if area[(x, y - 1)] == '.':
        neighbours.append((x, y - 1))

    if area[(x, y + 1)] == '.':
        neighbours.append((x, y + 1))

    if area[(x + 1, y)] == '.':
        neighbours.append((x + 1, y))

    if area[(x - 1, y)] == '.':
        neighbours.append((x - 1, y))

    return neighbours


# Run the search again, this time from the oxygen location
seen, queue = set([oxygen]), deque([[oxygen]])
time = 0
while queue:
    path = queue.popleft()

    if len(path) > time:
        time = len(path)

    pos = path[-1]

    for neighbour in nb(pos):
        x, y = neighbour
        if (x, y) not in seen:
            seen.add((x, y))

            new_path = list(path)
            new_path.append((x, y))

            queue.append(new_path)

print(time - 1)

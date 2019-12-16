from collections import defaultdict, deque
from intcode import Intcode
import enum


class Direction(enum.Enum):
    North = 1
    South = 2
    East = 3
    West = 4


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return (self.x, self.y)

    def move(self, direction):

        if direction == Direction.North:
            intcode.send(Direction.North)
            status = intcode.receive()
            if status:
                self.y -= 1

        if direction == Direction.South:
            intcode.send(Direction.South)
            status = intcode.receive()
            if status:
                self.y += 1

        if direction == Direction.West:
            intcode.send(Direction.West)
            status = intcode.receive()
            if status:
                self.x += 1

        if direction == Direction.East:
            intcode.send(Direction.East)
            status = intcode.receive()
            if status:
                self.x -= 1

        if status == 2:
            print(f"I found the oxygen system at {self.x},{self.y}")

        if status == 0:
            print(f"I hit a wall at {self.x},{self.y}")

    def get_neighbours(self):

        neighbours = []

        # Try North
        intcode.send(Direction.North)
        status = intcode.receive()
        if status:
            neighbours.append((self.x, self.y - 1, Direction.North))

            # Move back
            intcode.send(Direction.South)
            _ = intcode.receive()

        # Try South
        intcode.send(Direction.South)
        status = intcode.receive()
        if status:
            neighbours.append((self.x, self.y + 1, Direction.South))

            # Move back
            intcode.send(Direction.North)
            _ = intcode.receive()

        # Try West
        intcode.send(Direction.West)
        status = intcode.receive()
        if status:
            neighbours.append((self.x + 1, self.y, Direction.West))

            # Move back
            intcode.send(Direction.East)
            _ = intcode.receive()

        # Try East
        intcode.send(Direction.East)
        status = intcode.receive()
        if status:
            neighbours.append((self.x - 1, self.y, Direction.East))

            # Move back
            intcode.send(Direction.West)
            _ = intcode.receive()

        return neighbours


memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

intcode = Intcode(memory)

robot = Robot(0, 0)
seen, queue = set([(0, 0)]), deque([[(0, 0, Direction.North)]])

while queue:
    path = queue.popleft()

    robot.take_path(path, reverse=False)

    for neighbour in robot.get_neighbours():
        if neighbour not in seen:
            seen.add(neighbour)
            queue.append(neighbour)
    break

    robot.take_path(path, reverse=True)

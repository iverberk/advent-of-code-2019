from collections import defaultdict, deque
import operator

from intcode import Intcode

# Direction deltas
deltas = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])
left, right = 1, -1

# Initialize to UP (first) delta
direction = deltas[0]
position = (0, 0)

panels = defaultdict(int)
panels[position] = 0
painted = set()

memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

intcode = Intcode(memory)

while True:
    intcode.send(panels[position])

    color = intcode.receive()
    if color is None:
        break

    turn = intcode.receive()
    if turn is None:
        break

    panels[position] = color
    painted.add(position)

    deltas.rotate(left) if turn == 0 else deltas.rotate(right)

    position = tuple(map(operator.add, position, deltas[0]))

print(len(painted))

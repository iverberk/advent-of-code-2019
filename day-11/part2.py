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
panels[position] = 1

memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

intcode = Intcode(memory)
min_x, max_x, min_y, max_y = 0, 0, 0, 0
while True:
    intcode.send(panels[position])

    color = intcode.receive()
    if color is None:
        break

    turn = intcode.receive()
    if turn is None:
        break

    panels[position] = color

    deltas.rotate(left) if turn == 0 else deltas.rotate(right)

    position = tuple(map(operator.add, position, deltas[0]))

    # Keep track of the minimum and maximum coordinates
    x, y = position
    if x < min_x:
        min_x = x
    if x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    if y > max_y:
        max_y = y

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        print('#' if panels[(x, y)] else ' ', end='')
    print()

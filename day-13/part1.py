from collections import defaultdict
from intcode import Intcode

memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

intcode = Intcode(memory)

blocks = 0

while True:
    x = intcode.receive()
    y = intcode.receive()
    tile = intcode.receive()

    if None in [x, y, tile]:
        break

    if tile == 2:
        blocks += 1

print(blocks)

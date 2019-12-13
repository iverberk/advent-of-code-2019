from collections import defaultdict
from intcode import Intcode

memory = defaultdict(int)
with open('input') as f:
    for pos, x in enumerate(f.readline().strip().split(',')):
        memory[pos] = int(x)

# Play for free!
memory[0] = 2

intcode = Intcode(memory)

joystick, score, pad = 0, 0, None

while True:

    intcode.send(joystick)

    x = intcode.receive()
    y = intcode.receive()
    out = intcode.receive()

    if None in [x, y, out]:
        print(score)
        break

    # Pad update
    if out == 3:
        pad = (x, y)

    # Ball update
    if out == 4 and pad:
        px, py = pad
        if px > x:
            joystick = -1
        elif px == x:
            joystick = 0
        else:
            joystick = 1

    # Update the score
    if x == -1:
        score = out

from intcode import Intcode

with open('input') as f:

    memory = {pos: int(x) for pos, x in enumerate(f.readline().split(','))}

    intcode = Intcode(memory)
    intcode.send(1)

    print(intcode.receive())

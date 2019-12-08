from itertools import permutations

from intcode import Intcode

with open('input') as f:

    memory = [int(x) for x in f.readline().split(',')]

    max_boost = 0
    for phases in permutations(range(0, 5)):

        boost = 0
        for phase in phases:

            amplifier = Intcode(memory)

            amplifier.send(phase)
            amplifier.send(boost)

            boost = amplifier.receive()

            if boost > max_boost:
                max_boost = boost

    print(max_boost)

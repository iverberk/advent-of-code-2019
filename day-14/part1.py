from collections import defaultdict
from math import ceil

output_chemicals = defaultdict(list)

with open('input') as f:
    for reaction in f:
        if not reaction.strip():
            continue

        left, right = reaction.strip().split(' => ')

        quantity, chemical = right.split(' ')

        inputs = [input.split(' ') for input in left.split(', ')]
        output_chemicals[chemical] = [int(quantity)] + inputs

extra = defaultdict(int)


def produce(chemical, quantity=1):

    ores = 0

    for _ in range(quantity):
        if extra[chemical] > 0:
            extra[chemical] -= 1
            quantity -= 1

    if chemical == 'ORE':
        return quantity

    amount, *input_chemicals = output_chemicals[chemical]

    extra[chemical] += (ceil(quantity / amount) * amount) - quantity

    for input_chemical in input_chemicals:

        input_quantity, input_chemical = input_chemical
        ores += produce(input_chemical, int(input_quantity) * ceil(quantity / amount))

    return ores

print(produce('FUEL'))

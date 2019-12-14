from collections import defaultdict

output_chemicals = defaultdict(list)

with open('test') as f:
    for reaction in f:
        if not reaction.strip():
            continue

        left, right = reaction.strip().split(' => ')

        quantity, chemical = right.split(' ')

        inputs = [input.split(' ') for input in left.split(', ')]
        output_chemicals[chemical] = [int(quantity)] + inputs


ores = 0
extra = defaultdict(int)


def process(output_chemical, output_quantity=1, input_chemical=None, input_quantity=0):

    if extra[input_chemical] > 0:
        extra[input_chemical] -= 1
        return

    print("INPUT:", output_quantity, output_chemical, input_quantity, input_chemical)

    # End of the line, calculate ores
    if output_chemical == 'ORE':
        extra[input_chemical] += output_quantity - 1

        print("ores: ", output_quantity, extra)
        return

    m = output_quantity

    output_quantity, *input_chemicals = output_chemicals[output_chemical]

    for _ in range(m):

        for input_chemical in input_chemicals:

            input_quantity, input_chemical = input_chemical

            process(input_chemical, int(input_quantity), output_chemical, int(output_quantity))

            break

print(process('FUEL'))

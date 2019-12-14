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


def process(output_chemical, output_quantity=1, input_chemical=None, input_quantity=0, required_output=1):

    # print("INPUT:", output_quantity, output_chemical, input_quantity, input_chemical, required_output)
    # print()

    # End of the line, calculate ores
    if output_chemical == 'ORE':

        print("INPUT:", output_quantity, output_chemical, input_quantity, input_chemical, required_output)
        ores = output_quantity * ((required_output // input_quantity) + (required_output % input_quantity > 0))

        print(ores, extra)
        return

    output_quantity, *input_chemicals = output_chemicals[output_chemical]

    for input_chemical in input_chemicals:

        input_quantity, input_chemical = input_chemical

        process(input_chemical, int(input_quantity), output_chemical, int(output_quantity))

print(process('FUEL'))
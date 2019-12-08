from collections import defaultdict

size = 25 * 6
layers = defaultdict(list)

with open('input') as f:
    for image in f:
        for index, digit in enumerate(image.strip()):
            layers[index // size].append(int(digit))

    layer = min(layers, key=lambda layer: layers[layer].count(0))

print(layers[layer].count(1) * layers[layer].count(2))

from collections import defaultdict

wide, tall = 25, 6
size = wide * tall
layers = defaultdict(list)
colors = {0: ' ', 1: '#'}

with open('input') as f:
    for image in f:
        for index, digit in enumerate(image.strip()):
            layers[index // size].append(int(digit))

    for y in range(tall):
        for x in range(wide):
            index = y * wide + x
            for pixels in layers.values():
                if pixels[index] != 2:
                    print(colors[pixels[index]], end='')
                    break
        print()

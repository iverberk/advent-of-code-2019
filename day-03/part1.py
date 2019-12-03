def calculate_path(moves):

    locations = set()
    x, y, time = 0, 0, 0

    for move in moves:

        direction = move[0]
        amount = int(move[1:])

        for _ in range(0, amount):

            if direction == 'U': y += 1
            if direction == 'D': y -= 1
            if direction == 'R': x += 1
            if direction == 'L': x -= 1

            locations.add((x, y))

    return locations


with open('input') as f:

    moves = f.readline().strip().split(',')
    p1_path = calculate_path(moves)

    moves = f.readline().strip().split(',')
    p2_path = calculate_path(moves)

    crossings = p1_path.intersection(p2_path)

    print(min([abs(x)+abs(y) for x, y in crossings]))

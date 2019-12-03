def calculate_path(moves):

    locations = {}
    x, y, time = 0, 0, 0

    for move in moves:

        direction = move[0]
        amount = int(move[1:])

        for _ in range(0, amount):
            time += 1

            if direction == 'U': y += 1
            if direction == 'D': y -= 1
            if direction == 'R': x += 1
            if direction == 'L': x -= 1

            locations[(x, y)] = locations[(x,y)] if (x,y) in locations else time

    return locations


with open('input') as f:

    moves = f.readline().strip().split(',')
    p1_path = calculate_path(moves)

    moves = f.readline().strip().split(',')
    p2_path = calculate_path(moves)

    crossings = p1_path.keys() & p2_path.keys()

    print(min([p1_path[crossing] + p2_path[crossing] for crossing in crossings]))

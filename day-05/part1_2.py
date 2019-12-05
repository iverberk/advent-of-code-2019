with open('input') as f:
    memory = [int(x) for x in f.readline().split(',')]

    iptr = 0
    iwidth = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

    def get_parameter(position, mode):
        return memory[position] if mode == 1 else memory[memory[position]]

    while memory[iptr] != 99:

        opcode = memory[iptr] % 100
        modes = [
            memory[iptr] // 100 % 10,
            memory[iptr] // 1000 % 10,
            memory[iptr] // 10000 % 10,
        ]

        if opcode == 1:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            p3 = memory[iptr + 3]

            memory[p3] = p1 + p2

        elif opcode == 2:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            p3 = memory[iptr + 3]

            memory[p3] = p1 * p2

        elif opcode == 3:
            memory[memory[iptr + 1]] = int(input("Enter a number: "))

        elif opcode == 4:
            print(memory[memory[iptr + 1]])

        elif opcode == 5:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            if p1 != 0:
                iptr = p2
                continue

        elif opcode == 6:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            if p1 == 0:
                iptr = p2
                continue

        elif opcode == 7:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            p3 = memory[iptr + 3]
            memory[p3] = 1 if p1 < p2 else 0

        elif opcode == 8:
            p1 = get_parameter(iptr + 1, modes[0])
            p2 = get_parameter(iptr + 2, modes[1])
            p3 = memory[iptr + 3]
            memory[p3] = 1 if p1 == p2 else 0

        else:
            print("Unknown opcode encountered. Halting")
            quit()

        iptr += iwidth[opcode]

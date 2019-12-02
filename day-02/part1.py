with open('input') as f:
    memory = [int(x) for x in f.readline().split(',')]

    # Initialize memory
    memory[1], memory[2] = 12, 2

    iptr = 0
    while memory[iptr] != 99:

        (opcode, p1, p2, p3) = memory[iptr:iptr+4]

        if opcode == 1:
            memory[p3] = memory[p1] + memory[p2]
        elif opcode == 2:
            memory[p3] = memory[p1] * memory[p2]
        else:
            print("Unknown opcode encountered. Halting")
            quit()

        iptr += 4

print(memory[0])

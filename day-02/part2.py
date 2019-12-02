with open('input') as f:
    base_memory = [int(x) for x in f.readline().split(',')]

    for noun in range(0, 100):
        for verb in range(0, 100):

            memory = base_memory.copy()

            memory[1], memory[2] = noun, verb

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

            if memory[0] == 19690720:
                print("noun: {}, verb: {}, answer: {}".format(noun, verb, 100 * noun + verb))

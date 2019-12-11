class Intcode:

    def __init__(self, memory, name='Intcode'):
        self.trace = False
        self.name = name
        self.iptr = 0
        self.memory = memory.copy()
        self.__relative_base = 0
        self.__input = None
        self.__output = None
        self.instructions = {
            1: self.__add,
            2: self.__mul,
            3: self.__in,
            4: self.__out,
            5: self.__jnz,
            6: self.__jz,
            7: self.__lt,
            8: self.__eq,
            9: self.__rb
        }

        self.generator = self.__start()
        next(self.generator)

    def send(self, value):
        try:
            self.generator.send(value)
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'send' hit StopIteration")

    def receive(self):
        try:
            for output in self.generator:
                if output is not None:
                    next(self.generator)
                    return output
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'receive' hit StopIteration")
            return output

    def __get_parameter(self, position, mode):
        if mode == 0:
            return self.memory[self.memory[position]]
        elif mode == 1:
            return self.memory[position]
        elif mode == 2:
            return self.memory[self.memory[position] + self.__relative_base]
        else:
            print("Unknown mode, halting.")
            quit()

    def __get_input_position(self, iptr, mode):
        if mode == 0:
            return self.memory[iptr]
        elif mode == 2:
            return self.memory[iptr] + self.__relative_base
        else:
            print(f"Wrong input mode: {mode}. Halting.")
            quit()

    def __add(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        p3 = self.__get_input_position(self.iptr + 3, modes[2])

        self.memory[p3] = p1 + p2
        self.iptr += 4

    def __mul(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        p3 = self.__get_input_position(self.iptr + 3, modes[2])

        self.memory[p3] = p1 * p2
        self.iptr += 4

    def __in(self, modes):
        position = self.__get_input_position(self.iptr + 1, modes[0])
        self.memory[position] = self.__input
        self.__input = None
        self.iptr += 2

    def __out(self, modes=None):
        self.__output = self.__get_parameter(self.iptr + 1, modes[0])
        self.iptr += 2

    def __jnz(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        if p1 != 0:
            self.iptr = p2
        else:
            self.iptr += 3

    def __jz(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        if p1 == 0:
            self.iptr = p2
        else:
            self.iptr += 3

    def __lt(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        p3 = self.__get_input_position(self.iptr + 3, modes[2])

        self.memory[p3] = 1 if p1 < p2 else 0
        self.iptr += 4

    def __eq(self, modes):
        p1 = self.__get_parameter(self.iptr + 1, modes[0])
        p2 = self.__get_parameter(self.iptr + 2, modes[1])
        p3 = self.__get_input_position(self.iptr + 3, modes[2])

        self.memory[p3] = 1 if p1 == p2 else 0
        self.iptr += 4

    def __rb(self, modes):
        self.__relative_base += self.__get_parameter(self.iptr + 1, modes[0])
        self.iptr += 2

    def __start(self):

        while self.memory[self.iptr] != 99:

            if self.trace:
                print(f"{self.name}: processing instruction {self.iptr}")

            input = yield
            if input is not None:
                if self.trace:
                    print(f"{self.name}: received {input}")
                self.__input = input

            opcode = self.memory[self.iptr] % 100
            modes = [
                self.memory[self.iptr] // 100 % 10,
                self.memory[self.iptr] // 1000 % 10,
                self.memory[self.iptr] // 10000 % 10,
            ]

            if opcode in self.instructions:
                if self.trace:
                    print(f"{self.name}: opcode: {opcode}, input: {self.__input}")

                # Loop until we have the required input
                if opcode == 3 and self.__input is None:
                    if self.trace:
                        print("Waiting for input")
                    continue

                # Excute the opcode
                self.instructions[opcode](modes)
            else:
                print("Unknown opcode encountered. Halting")
                quit()

            if self.__output is not None:
                if self.trace:
                    print(f"{self.name}: sent {self.__output}")
                yield self.__output
                self.__output = None

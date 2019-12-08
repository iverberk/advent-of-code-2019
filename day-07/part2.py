from itertools import permutations, cycle

from intcode import Intcode

names = 'ABCDE'


def generate_amps(phases, memory):

    amps = {}

    # Create and initialize five amplifiers
    for amp in range(len(names)):

        # Create amplifier
        amplifier = Intcode(memory, names[amp])

        # Send amplifier phase
        amplifier.send(phases[amp])

        # Store the amplifier
        amps[names[amp]] = amplifier

    return amps


with open('input') as f:

    memory = [int(x) for x in f.readline().split(',')]

    max_signal = 0
    for phases in permutations(range(5, 10)):

        amps = generate_amps(phases, memory)

        signal = 0
        for amp in cycle(names):

            amps[amp].send(signal)

            signal = amps[amp].receive()
            if signal is None:
                break

            if signal > max_signal:
                max_signal = signal

    print(max_signal)

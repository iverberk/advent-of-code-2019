fuel = 0

with open('input') as f:
    for mass in f:
        mass = int(mass)
        while mass > 5:
            mass = mass // 3 - 2
            fuel += mass

print(fuel)

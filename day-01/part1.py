fuel = 0

with open('input') as f:
    for mass in f:
        fuel += int(mass) // 3 - 2

print(fuel)

limit, valid, start, end = 6, 0, 130254, 678275

for password in range(start, end):

    password = str(password)

    if password != ''.join(sorted(password)):
        continue

    pos = 0
    while pos < limit:

        matched = 1

        for n in range(pos+1, limit):
            if password[pos] == password[n]:
                pos += 1
                matched += 1

        pos += 1

        if matched > 1:
            valid += 1
            break

print(valid)

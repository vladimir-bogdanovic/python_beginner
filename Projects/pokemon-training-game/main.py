import random

rand_num = str(random.randrange(9999))
print(rand_num)
list =list(rand_num)

min_val = 9
max_val = 0

for digit in list:
    digit = int(digit)
    if digit < min_val:
        min_val = digit
    if digit > max_val:
        max_val = digit

print("Minimum:", min_val)
print("Maximum:", max_val)



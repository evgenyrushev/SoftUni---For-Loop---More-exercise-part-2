number_rounds = int(input())

score = 0

zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_nine = 0
thirty_to_nine = 0
forty_to_fifty = 0
invalid = 0

for x in range(number_rounds):
    current = int(input())

    if 0 <= current <= 9:
        score += (current * 0.20)
        zero_to_nine += 1
    elif 10 <= current <= 19:
        score += (current * 0.30)
        ten_to_nineteen += 1
    elif 20 <= current <= 29:
        score += (current * 0.40)
        twenty_to_nine += 1
    elif 30 <= current <= 39:
        score += 50
        thirty_to_nine += 1
    elif 40 <= current <= 50:
        score += 100
        forty_to_fifty += 1
    elif current > 50 or current < 0:
        score = score / 2
        invalid += 1
amount = zero_to_nine + ten_to_nineteen + twenty_to_nine + thirty_to_nine + forty_to_fifty + invalid

print(F"{score:.2f}")
print(f"From 0 to 9: {zero_to_nine / amount * 100:.2f}%")
print(f"From 10 to 19: {ten_to_nineteen / amount * 100:.2f}%")
print(f"From 20 to 29: {twenty_to_nine / amount * 100:.2f}%")
print(f"From 30 to 39: {thirty_to_nine / amount * 100:.2f}%")
print(f"From 40 to 50: {forty_to_fifty / amount * 100:.2f}%")
print(f"Invalid numbers: {invalid / amount * 100:.2f}%")




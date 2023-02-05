stadium_capacity = int(input())
number_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for x in range(number_fans):
    sector = input()

    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

total_fans = fans_b + fans_v + fans_a + fans_g

print(f"{fans_a / number_fans * 100:.2f}%")
print(f"{fans_b / number_fans * 100:.2f}%")
print(f"{fans_v / number_fans * 100:.2f}%")
print(f"{fans_g / number_fans * 100:.2f}%")
print(f"{total_fans / stadium_capacity * 100:.2f}%")

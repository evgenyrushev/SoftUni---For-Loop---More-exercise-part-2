months = int(input())

water = 0
internet = 0
others = 0
average = 0
electric = 0

for x in range(months):
    tok = float(input())

    water = x * 20 + 20
    internet = x * 15 + 15
    electric += tok

others = (water + internet + electric) * 1.20
average = (water + internet + electric + others) / months

print(f"Electricity: {electric:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")



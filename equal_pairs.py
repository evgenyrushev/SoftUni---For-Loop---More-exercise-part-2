n = int(input())
previous_sum = int(input()) + int(input())
max_diff = 0

for _ in range(n - 1):
    currentSum = int(input()) + int(input())

    if abs(previous_sum - currentSum) > max_diff:
        max_diff = abs(previous_sum - currentSum)

    previous_sum = currentSum

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")






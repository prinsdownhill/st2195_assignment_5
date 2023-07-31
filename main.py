def is_divisible_by_k(x, k):
    return x % k == 0

x = []
for i in range(1, 100):
    if is_divisible_by_k(i, 2):
        x.append(i)
    elif is_divisible_by_k(i, 5):
        x.append(i)
    elif is_divisible_by_k(i, 7):
        x.append(i)

print(sum(x))

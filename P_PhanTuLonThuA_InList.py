def find_nth_largest(lst, a):
    return sorted(lst, reverse=True)[a - 1] if 0 < a <= len(lst) else None

# Test function
L = [10, 20, 15, 30, 25]
a = 3
result = find_nth_largest(L, a)
print(f"Phan tu lon thu {a} trong Ds la: {result}")


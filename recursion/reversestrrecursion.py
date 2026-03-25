def reverse_str(n):
    if len(n) == 0:
        return n
    else:
        return reverse_str(n[1:]) + n[0]

print(reverse_str("hello"))  
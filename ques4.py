def total(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Total =", sum)

total(1, 2, 3)
total(5, 10, 15, 20)
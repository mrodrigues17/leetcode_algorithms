def square_root(num):
    counter = 0
    while counter * counter <= num:
        counter += 1
    return counter - 1

print(square_root(101))
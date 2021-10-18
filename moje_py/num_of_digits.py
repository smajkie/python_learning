def num_of_digits(num):
    counter = 0
    if num == 0:
        counter = 1
    elif num < 0:
        num = -num
        while num > 0:
            num = num//10
            counter = counter + 1
    while num > 0:
        num = num//10
        counter = counter + 1
    return(counter)

print(num_of_digits(-12381428))

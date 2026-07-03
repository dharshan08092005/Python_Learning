def multiply(*args):
    val = 1
    for num in args:
        val *= num

    print(f"Value of all args multiplied is {val}")


multiply(1,2,3,4,5,6,7,8)




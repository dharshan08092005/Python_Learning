def add(*args):
    sum = 0
    for _ in args:
        sum += _
    return sum

def sub(*args):
    diff = 0
    for _ in args:
        diff -= _
    return diff

def mul(*args):
    val = 1
    for _ in args:
        val *= _

    return val

def div(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2


while True:
    choice = int(input("""CALCULATOR
1.Addition
2.Subtraction
3.Multiply
4.Divide
5.Remainder
6.Exit
Enter your choice(1-6):"""))

    if choice == 6:
        print("Thanks...")
        break

    inp = input("Enter the values separated by spaces(ex: 1 2 3 ...):")

    lst = list(map(int, inp.split()))

    match choice:
        case 1:
            val = add(*lst)
            print(f"Addition value : {val}")
        case 2:
            val = sub(*lst)
            print(f"Subtraction value : {val}")
        case 3:
            val = mul(*lst)
            print(f"Multiplication value : {val}")
        case 4:
            val = div(*lst)
            print(f"Division value : {val}")
        case 5:
            val = remainder(*lst)
            print(f"Remainder value : {val}")
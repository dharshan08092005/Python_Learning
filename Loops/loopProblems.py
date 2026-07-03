"""1.Count how many factors a number has"""

num = 100
count = 2
for i in range(2, num // 2):
    if num % i == 0:
        count += 1
        print(count , i)

"""2.Check if a number is prime"""

num = 231
flag = False
for i in range(2, num//2):
    if num % i == 0:
        flag = True

if flag:
    print("Not Prime - Composite")
else:
    print("Prime")


"""3.Print all prime numbers from 1–100"""
start = 1
end = 100

count = 0
if start < 2: start = 2

for num in range(start, end + 1):
    flag = False
    for i in range(2, int(num * 0.5) + 1):
        if num % i == 0:
            flag = True
            break
    
    if not flag:
        count += 1
        print(num, "count =", count)


"""PATTERN PROGRAMMING"""

"""
1.
1
12
123
1234
12345
"""
for row in range(5):
    num = 1
    for col in range(row):
        print(num, end = "")
        num += 1
    print()

"""
2.
*
**
***
****
*****
"""

for row in range(5):
    for col in range(row):
        print("*", end = "")
    print()

"""
3.
*****
****
***
**
*
"""
for row in range(5,0,-1):
    for col in range(row):
        print("*", end = "")
    print()

"""
4.
1
22
333
4444
55555
"""
for row in range(1,6):
    for col in range(row):
        print(row, end="")
    print()

"""
5.
A B C
D E F
G H I
"""


val = 65
for row in range(3):
    for col in range(3):
        print(chr(val), end = "")
        val+=1
    print()

    
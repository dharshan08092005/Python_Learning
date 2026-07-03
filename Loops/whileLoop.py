"""While Loop Tutorial"""

i = 10
while(i > 0):
    print(i)
    i-=1

num = 7
table_val = 1
while(table_val <= 10):
    print(num, " X ", table_val, " = ", num * table_val)
    table_val += 1

mul_num = 20
while(mul_num >= 1):
    print(mul_num * 3)
    mul_num -= 1

power_num = 2
count = 0
val = 0
while(val < 1024):
    val = power_num ** count
    print(val)
    count += 1
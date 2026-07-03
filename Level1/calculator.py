# while(True):
#     string  = input()
#     print(eval(string))

"""
The Above method is dangerous because
eval() execute any string val
for ex:
string = "__import__("os").system("rm -rf /")"
!!!!!!
"""

num1,num2 = map(int, input().split())

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
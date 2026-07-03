""" For Loop tutorial"""


#Level 1
for _ in range(5):
    print("Hello")

for i in range(1,11):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

for i in range(1, 11):
    print(i * 5)

for i in range(10,1):
    print(i)

for i in range(1,11):
    print(i * i)

word = "Python"

for letter in word:
    print(letter)

for i in range(len(word)):
    if i % 2 == 0:
        print(word[i])
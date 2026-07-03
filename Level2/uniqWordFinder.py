string = "hi hello world how are you hello to you"

words = string.split(" ")

set = set()

duplicate_words = 0
for word in words:
    if word not in set:
        set.add(word)
    else:
        duplicate_words += 1

for word in set:
    print(word, end=" ")

print(f"\nTotal duplicate words is {duplicate_words}")


lst_items = [("pen",20),("pencil", 10), ("eraser", 5)]


max_item, max_price = 0,0
for item_name, item_price in lst_items:
    print(f"{item_name}'s price is {item_price} Rs")

    if(item_price > max_price):
        max_item = item_name
        max_price = item_price

print(f"Maximum price is {max_price} and the item is '{max_item}'")


#efficient way to find with lambda function

max_val = max(lst_items, key = lambda x:x[1])
min_val = min(lst_items, key = lambda x:x[1])

print(f"\nMaximum price is {max_val[1]} and the item is '{max_val[0]}'")

print(f"Minimum price is {min_val[1]} and the item is '{min_val[0]}'")


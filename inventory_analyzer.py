raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]
split_items=[tuple(item.split(":")) for item in raw_inventory]
#=[ (item, int(price)) for item, price in split_items]
tuple=[ (item, int(price)) for item, price in split_items]
print(tuple)
max_price_item=max(tuple,key=lambda x:x[1])
#print(max_price_item)
print(f"Item with most expensive price: {max_price_item[0]} at ${max_price_item[1]}")
min_price_item=min(tuple,key=lambda x:x[1])
print(f"Item with chepesst price: {min_price_item[0]} at ${min_price_item[1]}")

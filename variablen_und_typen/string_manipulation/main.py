grocery_items = "milk cheese bread apples oranges chicken"

first_space = grocery_items.find(" ")
second_space = grocery_items.find(" ", first_space + 1)
third_space = grocery_items.find(" ", second_space + 1)
fourth_space = grocery_items.find(" ", third_space + 1)
fifth_space = grocery_items.find(" ", fourth_space + 1)

dairy1 = grocery_items[0:first_space]
dairy2 = grocery_items[first_space+1:second_space]
bakery1 = grocery_items[second_space+1:third_space]

aisle = 5



print(f"We have dairy and bakery items: {dairy1}, {dairy2}, and {bakery1} in aisle {aisle}.")

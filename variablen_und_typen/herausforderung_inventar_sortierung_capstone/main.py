# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

space1 = items.find(", ")
space2 = items.find(", ", space1+1)

categories_space1 = categories.find(", ")

candy1 = items[0:space1]
candy2 = items[space1+2:space2]
dry_goods = items[space2+2:]

category1 = categories[0:categories_space1]
category2 = categories[categories_space1+2:]

bubblegum_price = "1.50"
chocolate_price = "2.00"
pasta_price = "5.40"

print(f"We have {candy1} for ${bubblegum_price} in the {category1}")
print(f"We have {candy2} for ${chocolate_price} in the {category1}")
print(f"We have {dry_goods} for ${pasta_price} in the {category2}")
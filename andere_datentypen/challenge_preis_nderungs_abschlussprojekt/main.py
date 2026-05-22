#1 Definition grocery_inventory
grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread" : ("Bakery", 2.99, 15),
    "Apples" : ("Produce", 1.50, 50),
}

#2 Preis prüfen und aktualisieren
egg_item = grocery_inventory.get("Eggs")
egg_category = egg_item[0]
egg_price = egg_item[1]
egg_number = egg_item[2]

if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs": (egg_category, egg_price - 1, egg_number)})
else:
    print("The price of Eggs is reasonable.")

#3 Neuen Artikel hinzufügen und grocery_inventory ausgeben
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#4 Bestand von "Milk" verwalten
milk_item = grocery_inventory.get("Milk")
milk_category = milk_item[0]
milk_price = milk_item[1]
milk_number = milk_item[2]

if milk_number < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk": (milk_category, milk_price, milk_number + 20)})
else:
    print("Milk has sufficient stock.")

#5 Artikel nach Preis entfernen
apples_item = grocery_inventory.get("Apples")
apples_category = apples_item[0]
apples_price = apples_item[1]
apples_number = apples_item[2]

if apples_price > 2.00:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

#6 Abschließende Ausgabe
print(f"Updated inventory: {grocery_inventory}")
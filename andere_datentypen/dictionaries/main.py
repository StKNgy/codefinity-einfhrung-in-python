#1 Definition eines Dictionaries mit dem Bezeichner grocery_inventory
grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce"),
}

#2 "Bread" abrufen und Details in bread_details speichern
bread_details = grocery_inventory.get("Bread")

# Ausgabe
print(f"Details of Bread: {bread_details}")

#3 Artikel "Cookies" hinzufügen: Produkt-ID: 143, Kategorie: "Bakery"
grocery_inventory.update({"Cookies": (143, "Bakery"),})

# Ausgabe
print(f"Inventory after adding Cookies: {grocery_inventory}")

#4 Artikel "Eggs" entfernen
grocery_inventory.pop("Eggs")

# Ausgabe
print(f"Inventory after removing Eggs: {grocery_inventory}")


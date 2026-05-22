# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#1 Vorkommen von "apples" in shelf und in apple_count speichern
apple_count = shelf.count("apples")

#2 Index des ersten Vorkommens von "Banana" in shelf in banana_index speichern
banana_index = shelf.index("bananas")

#4 Vorkommen von "grapes" in shelf zählen und in grapes_count speichern

print(f"Number of Apples: {apple_count}")
print(f"First Banana Index: {banana_index}")
#3 Bedingte Ausgabe: Anzahl Äpfel > 5?
print("Apples need to be restocked." if apple_count < 5 else "Apples are sufficiently stocked.")
#4 Bedingte Ausgabe: sind Trauben vorhanden?
print("Grapes need to be restocked." if shelf.count("grapes") <= 1 else "Grapes are sufficiently stocked.")
#5 Bedingte Ausgabe: sind Orangen vorhanden?
print(f"Oranges are at index: {shelf.index("oranges")}" if "oranges" in shelf else "Oranges are out of stock.")

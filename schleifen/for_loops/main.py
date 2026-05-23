prices = [12.99, 8.50, 15.75, 23.00, 7.25]

#1 Variable mit dem Bezeichner "total" deklarieren und mit dem Wert 0 initialisieren.
total = 0

#2 Iteriere mittels for-Schleife über die Liste "prices"
for price in prices:
    #3 addiere die Werte aus price zur Variablen "total"
    total += price

print(f"Total price: {total}")
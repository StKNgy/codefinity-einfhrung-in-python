meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

deli_dept = [meat, cheese, condiment]

# Ausgabe des Anfangszustands
print(f"Initial Deli List: {deli_dept}")

# Artikel auffüllen
if "Ham" in deli_dept[0] and deli_dept[0][2] < 100:
    deli_dept[0][2] = 100

# Erstllen der Liste seasonal_meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]

#Anhängen von seasonal_meat an deli_dept
deli_dept.append(seasonal_meat)

# Gewürze entfernen
deli_dept.remove(condiment)

# deli_dept sortieren
deli_dept.sort()

# Ausgabe aktualisierter Bestand
print(f"Updated Deli List: {deli_dept}")

prices = [29.99, 45.50, 12.75, 38.20]

#1 Anwendung einer for-Schleife mit den Funktionen range() und len()
#  um über die Liste prices zu iterieren
for index in range( len(prices) ):
    if index == 0:
        prices[index] -= prices[index] * 0.1
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    if index == 1:
        prices[index] -= prices[index] * 0.2
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    if index == 2:
        prices[index] -= prices[index] * 0.15
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
    if index == 3:
        prices[index] -= prices[index] * 0.05
        print(f"Updated price for item {index}: ${prices[index]:.2f}")
        
# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

for item, details in inventory.items():
    current_stock, min_stock, restock_qty, on_sale = details
    print("Processing started")
    #print(f"Item: {item}\t-> currentStock:\t{current_stock}\n\t\t-> minimum stock:\t{min_stock}\n\t\t-> restock quantity:\t{restock_qty}\n\t\t-> on sale:\t\t{on_sale}"+"\n"+("-"*45))

    print(f"Processing {item}")
    # Erhöhe den Bestand bei jeder Iteration
    while current_stock < min_stock:
        current_stock += restock_qty
        # Bestand aktualisieren
        inventory[item][0] = current_stock

    inventory[item][3] = current_stock > discount_threshold
    on_sale = inventory[item][3]

    print("Processing completed")
    #print(f"Item: {item}\t-> currentStock:\t{current_stock}\n\t\t-> minimum stock:\t{min_stock}\n\t\t-> restock quantity:\t{restock_qty}\n\t\t-> on sale:\t\t{on_sale}"+"\n"+("-"*45))
# Input variables
days_until_expiration = 5  # Example value
stock_level = 60  # Example value
product_type = "Perishable"  # Can be "Perishable" or "Non-Perishable"

rabatt = 0
info = ""

if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        rabatt = 30
        info = f"{rabatt}% discount applied"
    if days_until_expiration >= 4 and days_until_expiration <= 6 and stock_level > 50:
        rabatt = 20
        info = f"{rabatt}% discount applied"
    if days_until_expiration > 6 and stock_level <= 50:
        rabatt = 10
        info = f"{rabatt}% discount applied"
else:
    info = "No discount available for non-perishable items."


print(info)       
        
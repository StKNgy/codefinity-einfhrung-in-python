# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

info = "placeholder"

if product_type == "Fruits" and day_of_week == "Monday":
    info = "10% discount on Fruits today!"
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    info = "15% discount on Vegetables today!"
elif product_type == "Dairy" and day_of_week == "Wednesday":
    info = "20% discount on Dairy today!"
elif product_type == "Other":
    info = "No discount available."
else:
    info = "No special discounts today."

print(info)
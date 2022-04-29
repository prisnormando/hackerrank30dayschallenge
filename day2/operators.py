tip = meal_cost * tip_percent / 100
tax = meal_cost * tax_percent / 100
total_cost = meal_cost + tip + tax
    
print(round(total_cost))
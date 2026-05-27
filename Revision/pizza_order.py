
extra_toppings = "pepperoni, chicken, ham, mushrooms, onions, and mozzarella."
price_toppings = "10"

promo_code = "EXTRA_PIZZA123"
promo = 15
original_price= 15
discount_price= original_price - (original_price/100 * promo)

print("Hi welcome to Prime Pizzaria.")
pizza_type = input(f"Which kind of pizza would you like to order? We have {extra_toppings}")
order_toppings = input("Would you like any extra toppings?")
#Create a program for ordering pizza. 
#Users should be able to:
#Choose a pizza
#Add any extra toppings
#Add a PROMO code for a discount
#Output should be a receipt showing all choices, discounts and final cost. 
#Make the receipt look good! (using space, lines, etc. like ASCII art)

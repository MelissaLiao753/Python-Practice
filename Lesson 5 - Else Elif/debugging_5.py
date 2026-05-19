
#INITIAL VARIABLES
item_price = 50
gst = 1.12

#AGE DISCOUNT 
user_age = input("Enter your age: ")
user_age_int = int(user_age)

if user_age_int < 18:3

elif user_age_int == 18:
    discount = 10.0

elif user_age_int > 18:
    discount = 0.0

#FOLLOWING VARIABLES
initial_price = item_price - discount
final_price = initial_price * gst
final_price_int = int(final_price)

#FINAL PRICE 
print("The total is: ", final_price_int)

if final_price_int > 40:
    print("Expensive")
    
else:
    print("Affordable")
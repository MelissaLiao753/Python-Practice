#VARIABLES/CONSTANTS

MEMBER_STATUS = "GOLD"
row = int(input("Enter your seat row: ").strip())
has_ticket = input("Do you have a valid ticket? (yes/no): ")

if has_ticket.lower() == "yes":
    print("Access Denied. Please ensure you have a valid ticket before boarding.")

if row <= 8 and MEMBER_STATUS == "gold":
      print("Welcome to priority boarding! Please make your way on board now.")

elif row <= 8 or MEMBER_STATUS == "gold":
    print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")

elif row > 8 :
    print("Please wait for general boarding.")

destination = input("Enter your destination code: ")

if destination == "AKL" or "WLG":
    print("Flight is delayed 5 minutes.")
else:
    print("Hope you have wonderful travel. We're taking off soon.")
# PSEUDOCODE START
# IF NOT destination is equal to "CHC" THEN print "Flight is on time."
# ELSE print "Flight has been cancelled"
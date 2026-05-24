# Create a student email creator that uses first and last name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables
#Input variables
first_name = input("What's your first name?")
last_name = input("What's your last name?")
id_num = input("What's your id number?")


# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)
#Variables to certain data
first = str(first_name.strip().lower())
last = str(last_name.strip().lower())
id = str(id_num.strip())
id_num1 = int(id_num.strip())/10
# Output the final email address
print("Your email is "+ first+last+id +"@fake.school.nz")


# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10
print("Your temporary password is" + first.upper()+last.upper()+ str(id_num1))
# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user
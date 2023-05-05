
# Name
username =  str(input("Enter your name! "))

# Greetings
print("Welcome {}! This is the Force calculator made by franklin".format(username))

# Calculation
Acceleration = float(input("Add an acceleration (ms^2) : "))
Mass = float(input("Add mass (kg) : "))
Force = Mass * Acceleration 

# Results
print("Succesfull!" + " " + str(Force) + "N" + " " + "=" + " " + str(Mass) + " " + "x" + " " + str(Acceleration))
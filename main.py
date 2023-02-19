#Welcome Message
print("Welcome to week 4 assignment")

#Company name from user
company_name = input("Please enter the name of the company: ")
print(f"\n{company_name}!")

#Number of feet of fiber optic cable
feet_of_cable = input("Please enter the number of feet of cable! ")
feet_of_cable = float(feet_of_cable)

if feet_of_cable < 100:
  cost_of_cable = feet_of_cable * .87
elif feet_of_cable < 250:
  cost_of_cable = feet_of_cable * .80
elif feet_of_cable > 500:
  cost_of_cable = feet_of_cable * .50

#Calculated information and Company Name
message = company_name + " The cost is: " + str(cost_of_cable)

print(message)
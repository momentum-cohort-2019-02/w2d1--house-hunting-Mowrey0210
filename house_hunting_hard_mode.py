# Hard_Mode------------------------------------------------------------

annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
r = float(input("Enter the expected annual rate of return:") or .04)
total_cost = int(input("Enter the cost of your dream home:"))
portion_down_payment= float(input("Enter the percent of your home's cost to save as a down payment:") or .25)

# if not r:
#     r=.04

# if not portion_down_payment: 
#     portion_down_payment = .25

current_savings = 0
count= 0
percentage_of_savings = (annual_salary/12)*portion_saved
down_payment = (total_cost*portion_down_payment)


# This works because a blank value is false. Therefore you write an if statement using the keyword not which specifies that if the variable r is empty(it will give the variable r the value .04)


while current_savings < down_payment:
    roi = current_savings*(r/12)
    current_savings = current_savings+percentage_of_savings + roi

    count+= 1    

print("Enter your annual salary:" + " " + str(annual_salary))
print("Enter the percent of your salary to save, as a decimal:" + " " + str(portion_saved))
print("Enter the expected annual rate of return [0.04]:" + " " + str(r))
print("Enter the cost of your dream home:" + " " + str(total_cost))
print("Enter the percent of your home's cost to save as a down payment [0.25]:" + " " + str(portion_down_payment))
print("Number of months:" + " " + str(count))

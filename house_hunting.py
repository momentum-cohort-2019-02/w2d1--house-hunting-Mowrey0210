annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))


current_savings = 0
count= 0
percentage_of_savings = (annual_salary/12)*portion_saved
portion_down_payment= .25
down_payment = (total_cost*portion_down_payment)


while current_savings < down_payment:
    roi = current_savings*(.04/12)
    current_savings = current_savings+percentage_of_savings + roi
    count+= 1    

print("Enter your annual salary:" + " " + str(annual_salary))
print("Enter the percent of your salary to save, as a decimal:" + " " + str(portion_saved))
print("Enter the cost of your dream home:" + " " + str(total_cost))
print("Number of months:" + " " + str(count))


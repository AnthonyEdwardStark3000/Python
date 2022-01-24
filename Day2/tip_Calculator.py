#Tip calculator
print("*************** Welcome to tip calculator ***************\n")
total_bill = float(input("Enter the total bill cost :"))
percentage = float(input("Enter the percentage of tip you want to provide :"))
persons = int(input("Enter the number of persons:"))
tip_percent = percentage / 100
tip_amount = tip_percent * total_bill
total_payable_bill = total_bill + tip_amount
each_person = total_payable_bill / persons
print(f"The {total_bill} $ bill demands ech person to pay {each_person} $")

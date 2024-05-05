from bill import Bill
from flatmate import Flatmate
from pdf_reports import PDFReport

# Gathering user input via command line interface
bill_amount = float(input("Hello, please enter the bill amount: "))
bill_period = input("Please enter the bill period: ")

name_1 = input("What is your name? ")
days_in_house_1 = int(input(f"How many days did {name_1} stay in the house?"))

name_2 = input("What is your flatmate's name? ")
days_in_house_2 = int(input(f"How many days did {name_2} stay in the house?"))

my_bill = Bill(bill_amount, bill_period)
flatmate_1 = Flatmate(name=name_1, days_in_house=days_in_house_1)
flatmate_2 = Flatmate(name=name_2, days_in_house=days_in_house_2)

print(f"{name_1} pays: £", round(flatmate_1.pays(bill=my_bill, other_flatmate=flatmate_2), ndigits=2))
print(f"{name_2} pays: £", round(flatmate_2.pays(bill=my_bill, other_flatmate=flatmate_1), ndigits=2))

pdf_report = PDFReport(filename=f"{my_bill.period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, bill=my_bill)

print("Your PDF bill report has been generated in the files directory.")

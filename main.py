from fpdf import FPDF

class Bill:
    """
    Contains data about a bill such as the total amount and the period of the bill.
    """
    def __init__(self, amount, period, due_date=None):
        self.amount = amount
        self.period = period
        self.due_date = due_date


class Flatmate:
    """Contains data about a person living in the flat and how much they owe."""
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weighting = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        amount_to_pay = bill.amount * weighting
        return amount_to_pay

class PDFReport:
    """
    Creates a PDF file to summarise data about the flatmates,
    including their names and how much they owe, and the period of their bill.
    Using the fpdf package.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2):
        pass

# Testing
my_bill = Bill(amount=120, period="March 2024")
Euan = Flatmate(name="Euan", days_in_house=20)
Sol = Flatmate(name="Sol", days_in_house=30)

print(Euan.pays(bill=my_bill, other_flatmate=Sol))

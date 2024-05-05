class Flatmate:
    """Contains data about a person living in the flat and how much they owe."""

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weighting = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        amount_to_pay = bill.amount * weighting
        return amount_to_pay

class Bill:
    """
    Contains data about a bill such as the total amount and the period of the bill.
    """

    def __init__(self, amount, period, due_date=None):
        self.amount = amount
        self.period = period
        self.due_date = due_date

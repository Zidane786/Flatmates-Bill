class Bill:
    """
    Object that contain total bill amount and the period of
    the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create Flatmate person who stays in flat and pays a
    share of bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        """
        :param bill:Bill class object
        :return: share of bill this flatmate object needs
                 to pay.
        """
        # for now to see everything is working lets share bill by 50/50 ratio
        # later we will write code for bill share base on amount of day stay in house
        return bill.amount / 50


class PdfReport:
    """
    Generate Pdf file stating:-
            the total Bill,
            the names of flatmate,
            the period,
            and how much each of flatmate has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        :param flatmate1: Flatmate class object (flatmate1)
        :param flatmate2: Flatmate class object (flatmate2)
        :param bill: Bill class object (bill)
        :return: generate PDF file for Flatmate Bill Report.
        """
        pass


# creating Bill object
the_bill = Bill(amount=120, period="October 2021")

# creating Flatmates object
zidane = Flatmate(name="Zidane", days_in_house=20)
aadil = Flatmate(name="Aadil", days_in_house=25)

# printing bill flatmate object need to pay
# we will pay bill 50/50 for now later we will write code for paying base on no. of day stay in flat
print(f"{zidane.name} needs to pay is:- {zidane.pays(bill=the_bill)}")
print(f"{aadil.name} needs to pay is :- {aadil.pays(bill=the_bill)}")

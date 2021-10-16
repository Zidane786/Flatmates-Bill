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
        self.name = name.title()
        self.days_in_house = days_in_house

    def pays(self, bill):
        """
        :param bill:Bill class object
        :return: share of bill this flatmate object needs
                 to pay.
        """
        # go and see design_&_logic.txt there we explain how we got below formula
        co_eff = self.days_in_house / total_days_both_flatmate_stay_in_house
        return bill.amount * co_eff  # this will return bill flatmate need to pay


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
the_bill = Bill(amount=int(input("Enter Bill Amount:-")),
                period=input("Enter Bill Period eg:August 2021:-"))

# creating Flatmates object
f1 = Flatmate(name=input("Enter the name of flatmate:-"),
              days_in_house=int(input("Enter no.of day stayed in flat:-")))
f2 = Flatmate(name=input("Enter the name of flatmate:-"),
              days_in_house=int(input("Enter no.of day stayed in flat:-")))

total_days_both_flatmate_stay_in_house = f1.days_in_house + f2.days_in_house

# printing bill flatmate object need to pay
# we will pay bill 50/50 for now later we will write code for paying base on no. of day stay in flat
print(f"{f1.name} needs to pay is:- {f1.pays(bill=the_bill):.2f}")
print(f"{f2.name} needs to pay is :- {f2.pays(bill=the_bill):.2f}")

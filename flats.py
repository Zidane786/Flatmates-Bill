"""
This File contain Bill Class and Flatmate class where Bill class will take info regarding
bill amount and bill period
whereas Flatmate class will take info regarding flatmate name and no. day stay in house for that
bill period and return the amount flatmate need to pay base on no. of day flatmate stay in house
"""


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

    def pays(self, bill, flatmate):
        """
        :param bill:Bill class object
        :param flatmate:Remaining Flatmate Object(i.e:-when
               self is f1 than this is f2 object  or visa versa)
        :return: share of bill this flatmate object needs
                 to pay.
        """
        # go and see design_&_logic.txt there we explain how we got below formula
        co_eff = self.days_in_house / (flatmate.days_in_house + self.days_in_house)
        to_pay = bill.amount * co_eff  # bill flatmate need to pay
        return float(f'{to_pay:.2f}')  # rounding of to_pay value so there are only 2 numbers after decimal point

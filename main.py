from fpdf import FPDF


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
        return float(f'{to_pay:.2f}')


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
        # generating PDF stating information
        pdf = FPDF(orientation='P', unit='pt', format='A4')  # create PDF file without pages or initialize FPDF instance
        # 1 pt = 1.33 pixel
        # adding page
        pdf.add_page()
        # Setting Font:-
        pdf.set_font(family='arial', style='BI', size=25)
        # adding cell
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)  # ln=1 i.e next line
        # border=1 means show rectangle(cell) border.
        # border=0 means don't show the rectangle(cell) border.
        # insert period label and value
        pdf.cell(w=100, h=40, txt="Period:-", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, ln=1)

        # insert total bill amount label and value
        pdf.cell(w=230, h=40, txt="Total Bill Amount:-", border=0)
        pdf.cell(w=100, h=40, txt=f'{bill.amount}', border=0, ln=1)  # go to next line

        # creating table having column with fields name,no. of day stays,amount to pay
        pdf.cell(w=20, ln=1)  # go to next line
        pdf.cell(w=130, h=40, txt='Name', border=1)
        pdf.cell(w=300, h=40, txt='Days stay in Flat', border=1)
        pdf.cell(w=120, h=40, txt='Amount', border=1, ln=1)  # next line
        # changing font
        pdf.set_font('arial', 'I', 20)

        # adding flatmate1 info in row 1:-
        pdf.cell(w=130, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=300, h=40, txt=f"{flatmate1.days_in_house}", border=1)
        pdf.cell(w=120, h=40, txt=f"{flatmate1.pays(bill, flatmate2)}", border=1, ln=1)

        # adding flatmate2 info in row 2:-
        pdf.cell(w=130, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=300, h=40, txt=f"{flatmate2.days_in_house}", border=1)
        pdf.cell(w=120, h=40, txt=f"{flatmate2.pays(bill, flatmate1)}", border=1, ln=1)
        pdf.output(self.filename)  # create PDF file with pass filename as parameter


the_bill = Bill(120, "December 2021")
f1 = Flatmate("zidane", 20)
f2 = Flatmate("aadil", 25)

# creating user input Bill object
# the_bill = Bill(amount=int(input("Enter Bill Amount:-")),
#                 period=input("Enter Bill Period eg:August 2021:-"))
# creating user input Flatmates object
# f1 = Flatmate(name=input("Enter the name of flatmate:-"),
#               days_in_house=int(input("Enter no.of day stayed in flat:-")))
# f2 = Flatmate(name=input("Enter the name of flatmate:-"),
#               days_in_house=int(input("Enter no.of day stayed in flat:-")))

# total_days_both_flatmate_stay_in_house = f1.days_in_house + f2.days_in_house
# commented since we pass remaining flatmate object in pays()


# printing bill flatmate object need to pay
# we will pay bill 50/50 for now later we will write code for paying base on no. of day stay in flat
print(f"{f1.name} needs to pay is:- {f1.pays(bill=the_bill, flatmate=f2)}")
print(f"{f2.name} needs to pay is :- {f2.pays(bill=the_bill, flatmate=f1)}")

# PdfReport object
pdf_report = PdfReport('flatmates_bill.pdf')
pdf_report.generate(flatmate1=f1, flatmate2=f2, bill=the_bill)

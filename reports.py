import os
import webbrowser
from fpdf import FPDF

"""
This file will generate pdf file for flatmates bill project
"""


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
        # adding page:-
        pdf.add_page()
        # Setting Font:-
        pdf.set_font(family='arial', style='BI', size=25)
        # adding icon
        pdf.image(name='files/home.jpeg', w=30, h=30)  # we place icon with width and height 30
        # adding Title using cell
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

        # changing current directory to files so that pdf saves there
        os.chdir('files')
        # creating pdf file
        pdf.output(self.filename)  # create PDF file with pass filename as parameter

        # below line will automatically open the pdf file in web browser
        # webbrowser.open(self.filename) for windows user windows will automatically create the path:-
        # i.e:-file://C://User/etc.
        # but in linux/mac we need to provide path manually so we will use below line for opening file in browser
        webbrowser.open("file://" + os.path.realpath(self.filename))  # for mac and linux user

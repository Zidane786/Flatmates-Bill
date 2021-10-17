from flats import Bill, Flatmate
from reports import PdfReport


if __name__ == "__main__":
    # creating user input Bill object
    bill_amount = float(input("Enter the Bill Amount:- "))
    bill_period = input("What is the Bill Period ? eg:August 2021:- ")
    the_bill = Bill(amount=bill_amount, period=bill_period)
    # creating user input Flatmates object
    name_1 = input("Enter the name of flatmate1:- ")
    days_in_house1 = int(input(f"Enter no.of days {name_1} stayed in flat during bill period:- "))
    f1 = Flatmate(name=name_1, days_in_house=days_in_house1)

    name_2 = input("Enter the name of flatmate2:- ")
    days_in_house2 = int(input(f"Enter no.of days {name_2} stayed in flat during bill period:- "))
    f2 = Flatmate(name=name_2, days_in_house=days_in_house2)

    # total_days_both_flatmate_stay_in_house = f1.days_in_house + f2.days_in_house
    # commented since we pass remaining flatmate object in pays()


    # printing bill flatmate object need to pay
    # we will pay bill 50/50 for now later we will write code for paying base on no. of day stay in flat
    print(f"{f1.name} needs to pay is:- {f1.pays(bill=the_bill, flatmate=f2)}")
    print(f"{f2.name} needs to pay is :- {f2.pays(bill=the_bill, flatmate=f1)}")

    # PdfReport object
    pdf_report = PdfReport(f'{the_bill.period}.pdf')
    pdf_report.generate(flatmate1=f1, flatmate2=f2, bill=the_bill)

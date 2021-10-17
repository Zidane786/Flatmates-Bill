from fpdf import FPDF

pdf = FPDF(orientation="P", unit='pt', format="A4", )  # 1pt=1.33 pixel
# above line will create PDF object(Document) but without pages
# so lets add page using add_page() method
pdf.add_page()  # this will create pdf page

# adding text to Pdf
# before adding text lets set font style,family,size
pdf.set_font(family="arial", style="B", size=25)
pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C",
         ln=1)  # align="C" --> keep text in center #ln=1 Go to next line
# w=200 of cell(rectangle/div) is 200 point
# w=0 means take entire horizontal length of pdf for rectangle
# border = 1 create the border of cell if we don't want that pass border=0
# unit is pt # think cell() as rectangle or <div> tag if you are familiar with HTML
pdf.cell(w=100,h=40,txt="Period:",border=1)
pdf.cell(w=150, h=40, txt="March 2021", border=1)

pdf.output("test1.pdf")  # it will create test1.pdf output file in current directory

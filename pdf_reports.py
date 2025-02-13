import webbrowser
import os
from fpdf import FPDF


class PDFReport:
    """
    Creates a PDF file to summarise data about the flatmates,
    including their names and how much they owe, and the period of their bill.
    Using the fpdf package.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate_1, flatmate_2, bill):
        flatmate_1_pays = "£" + str(round(flatmate_1.pays(bill=bill, other_flatmate=flatmate_2), 2))
        flatmate_2_pays = "£" + str(round(flatmate_2.pays(bill=bill, other_flatmate=flatmate_1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert the house logo
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill Summary", border=0, align='C', ln=1)

        # Insert period label
        pdf.set_font(family='Helvetica', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and amount due for the first flatmate
        pdf.set_font(family='Helvetica', size=14, style='')
        pdf.cell(w=100, h=30, txt=flatmate_1.name, border=0)
        pdf.cell(w=150, h=30, txt=flatmate_1_pays, border=0, ln=1)

        # Insert name and amount due for the second flatmate
        pdf.set_font(family='Helvetica', size=14, style='')
        pdf.cell(w=100, h=30, txt=flatmate_2.name, border=0)
        pdf.cell(w=150, h=30, txt=flatmate_2_pays, border=0, ln=1)

        # Generate PDF
        pdf.output(f"files/{self.filename}")

        # Change OS directory to "files", open the PDF (this only works on Windows)
        os.chdir("files")
        webbrowser.open(self.filename)

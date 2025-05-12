from fpdf import FPDF
from PIL import Image, ImageOps
import sys


class Print:
    def __init__(self, name):
        self._name = name

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.image("shirtificate.png", x=15, y=65, w=180)

        pdf.set_font('helvetica', size=50)
        pdf.cell(190, 40, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

        pdf.set_font('helvetica', style="b", size=25)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(190, 160, f"{self._name} took CS50", new_x="LMARGIN", new_y="NEXT", align='C')

        pdf.output("shirtificate.pdf")

    @property
    def name(self):
        return self._name

def main():
    person = Print(input("Name: ").strip())
    person.generate()

if __name__ == "__main__":
    main()

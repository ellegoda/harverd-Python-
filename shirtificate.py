from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.image("shirtificate.png", x=45, y=80, w=120)
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

    def generate_shirtificate(self, name):
        self.add_page()
        self.ln(100)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, name + " took CS50", align='C')


if __name__ == "__main__":
    pdf = Shirtificate(orientation='P', unit='mm', format='A4')
    user_name = input("Name: ")
    pdf.generate_shirtificate(user_name)
    pdf.output("shirtificate.pdf")

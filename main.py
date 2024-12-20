from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df=pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    #Header
    pdf.set_font(family="Times",style="B",size=20)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, txt=row["Topic"], ln=1, align="L", )
    for y in range(20, 280, 10):
        pdf.line(10, y, 200, y)

    #Footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="IB", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        #Footer
        pdf.ln(270)
        pdf.set_font(family="Times", style="IB", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for y in range(20, 280, 10):
            pdf.line(10, y, 200, y)

pdf.output("Output.pdf")
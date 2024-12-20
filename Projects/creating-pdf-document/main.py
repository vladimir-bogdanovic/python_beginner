from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

file_name = "crating_pdf2.pdf"
document_title = "sample"
title  = "technology"
subtitle = "the largest thing now"
text_lines = [
    "Technology makes us aware of",
    "the world around us"
]
image = "image.jpg"

# creating pdf object and setting title
pdf = canvas.Canvas(file_name)
pdf.setTitle(document_title)

# register font
font_path = r"C:\Users\MI-Store\Downloads\Jersey_15,Platypi,Roboto_Condensed\Platypi\static\Platypi-SemiBold.ttf"
font_name = "platypi"
pdfmetrics.registerFont(TTFont(font_name, font_path))

# set font for title
pdf.setFont(font_name, 36)
pdf.drawCentredString(250,750,title)

# creating subtitle
pdf.setFillColorRGB(0,0,222)
pdf.setFont("Courier-Bold", 22, )
pdf.drawCentredString(290, 700, subtitle)

# creating divider line
pdf.line(30,650, 550,650)

# creating: where to start text, setting font , color text, looping through text lines and assigning it to text and in the end drawText
text = pdf.beginText(40,580)
text.setFont("Courier", 13)
text.setFillColor(colors.red)
for line in text_lines:
    text.textLine(line)

pdf.drawText(text)

# adding image into file using drawInLineImage function
pdf.drawInlineImage("pngtree-blue-bird-vector-or-color-illustration-png-image_2013004.jpg",100, 170)

#saving pdf
pdf.save()
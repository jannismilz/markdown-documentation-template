from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

# Step 1: Open the PDF file and read its pages.
pdf_path = 'pdfs/chapters.pdf'
pdf = PdfReader(pdf_path)

# Step 2: Create a new PDF with page numbers.
width, height = letter
output = io.BytesIO()
c = canvas.Canvas(output, pagesize=letter)

for i in range(len(pdf.pages)):
    c.setFont("Helvetica", 10)
    c.drawString(37, 30, "Jannis Milz")
    c.drawRightString(width - 54, 30, f"{str(i + 1)} / {len(pdf.pages)}")
    c.setHorizScale(100)
    c.drawRightString(width - 50, height - 30, "Ein Name")
    c.showPage()

c.save()

# Move to the beginning of the StringIO buffer
output.seek(0)
new_pdf = PdfReader(output)

# Step 3: Merge the original PDF and the new PDF with page numbers.
pdf_writer = PdfWriter()

for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    page.merge_page(new_pdf.pages[i])
    pdf_writer.add_page(page)

# Step 4: Write to a new PDF file.
with open('pdfs/chapters.pdf', 'wb') as fh:
    pdf_writer.write(fh)

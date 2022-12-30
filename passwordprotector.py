from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass

pdfWriter = PdfFileWriter()

pdf = PdfFileReader("file.pdf")

for no in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(no))
    
password = getpass(prompt="Enter password:")

pdfWriter.encrypt(password)

with open('file3.pdf','wb') as f:
    pdfWriter.write(f)
    
    
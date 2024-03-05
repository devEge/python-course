from pdf2docx import Converter

pdf_file = "testPDF.pdf"
docx_file = "testDocx.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
print("Done")
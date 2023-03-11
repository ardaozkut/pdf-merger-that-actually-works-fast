import PyPDF2

pdf1 = open('math_kapak.pdf', 'rb')
pdf2 = open('Note 8 Mar 2023.pdf', 'rb')

pdf1_reader = PyPDF2.PdfReader(pdf1)
pdf2_reader = PyPDF2.PdfReader(pdf2)

pdf_writer = PyPDF2.PdfWriter()
for page_num in range(len(pdf1_reader.pages)):
    page = pdf1_reader.pages[page_num]
    pdf_writer.add_page(page)

for page_num in range(len(pdf2_reader.pages)):
    page = pdf2_reader.pages[page_num]
    pdf_writer.add_page(page)

output_pdf = open('merged_file.pdf', 'wb')
pdf_writer.write(output_pdf)

pdf1.close()
pdf2.close()
output_pdf.close()
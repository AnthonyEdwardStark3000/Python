import PyPDF2

file = PyPDF2.PdfFileReader(open('merged_pdf.pdf', 'rb'))
watermark_template = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

writer = PyPDF2.PdfFileWriter()

for page in range(file.getNumPages()):
    current_page = file.getPage(page)
    current_page.mergePage(watermark_template.getPage(0))
    writer.addPage(current_page)

    with open('watermarked_pdf.pdf','wb') as water:
        writer.write(water)
print(f'Done with the watermark of the file {file}')
import PyPDF2

with open('pdf-processing/dummy.pdf', 'rb') as file:
    pdf_file = PyPDF2.PdfFileReader(file)
    page_object = pdf_file.getPage(0)
    print(page_object.extractText())

    # Trying to rotate the pdf page
    page_object2 = pdf_file.getPage(0)
    print(page_object2.rotateClockwise(180))
    writer_file = PyPDF2.PdfFileWriter()
    writer_file.addPage(page_object2)
    with open('inverted.pdf', 'wb') as new_file:
        writer_file.write(new_file)

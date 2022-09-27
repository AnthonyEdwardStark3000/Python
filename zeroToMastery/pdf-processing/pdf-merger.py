import os
import sys
from PyPDF2 import PdfFileMerger, PdfReader
from os import path
directory = os.path.dirname(__file__)
inputs = sys.argv[1:]
pdfs_found = []
for file_name in inputs:
    if path.exists(f'{file_name}.pdf'):
        print(f'{file_name}')
        merger = PdfFileMerger()
        pdfs_found.append(file_name)

    else:
        print(
            f'Please check the file name as there is no file named as {file_name}.py in the directory {directory}')
for pdf_file in pdfs_found:
    merger.append(PdfReader(open(f'{pdf_file}.pdf', 'rb')))
    print(f'Wrote {pdf_file}.pdf')
merger.write('merged_pdf.pdf')
merger.close()
print('Completed the process of merging the pdf files')

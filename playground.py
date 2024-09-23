from glob import glob
from PyPDF2 import PdfMerger

file = glob('printQR/*.pdf')
file.sort()

merger = PdfMerger()

for pdf in file:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
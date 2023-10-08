from PyPDF2 import PdfMerger

#list of pdf files to be merged in list
pdfs = ['file1.pdf', 'file2.pdf']

merger = PdfMerger()

#append one file to another by append them
for pdf in pdfs:
    merger.append(pdf)


#merge the pdf and give output.pdf file
merger.write("result.pdf")

merger.close()
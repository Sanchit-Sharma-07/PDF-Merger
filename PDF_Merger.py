from pypdf import PdfWriter

merger = PdfWriter()
pdfs = []
n = int(input("How many pdfs you want to merge: "))

for i in range(0,n):
    name = input(f"Enter the name of your pdf{i + 1}:")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

#There are alot more operations on pdfs using pypdf. You can check more at their documentaion
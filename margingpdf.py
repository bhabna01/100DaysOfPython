from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["srcdoc.pdf", "1980.pdf", "1992.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

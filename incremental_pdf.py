from PyPDF2 import PdfMerger

merger = PdfMerger()

pdfs = ['Pagina1.pdf', 'Pagina2.pdf', 'Pagina3.pdf', 'Pagina4.pdf', 'Pagina5.pdf', 'Pagina6.pdf']

for pdf in pdfs:
    merger.append(pdf)


merger.write('documentos_cirurgia.pdf')

merger.close()
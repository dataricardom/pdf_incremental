from PyPDF2 import PdfMerger
from datetime import datetime

def pdf_incremental(caminho_pdfs):
    timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

    merger = PdfMerger()


    for pdf in caminho_pdfs:
        merger.append(pdf)

    nome_salvo = f'documentos_cirurgia_{timestamp}.pdf'
    merger.write(nome_salvo)

    merger.close()




"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
"""
import PyPDF2
import os

caminho_dos_pdfs = r'.\python-modulos\aula19-pypdf2\pdf'


novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        
        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
from tkinter import filedialog

import PyPDF2


class PDFToText:
    def __init__(self):
        self.pdf_file_obj = open(filedialog.askopenfilename(initialdir="C:/",
                                                            title="Nilay",
                                                            filetypes=(("PDF files", "*.pdf*"), ("all files", "*.*"))),
                                 'rb')

    def translate_pdf(self):
        pdfreader = PyPDF2.PdfReader(self.pdf_file_obj)
        x = len(pdfreader.pages)
        page_obj = pdfreader.pages[x - 1]
        text = page_obj.extract_text()
        return text

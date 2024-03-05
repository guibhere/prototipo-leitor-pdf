import pdf2image
from PIL import Image
import pytesseract
import tkinter as tk
from tkinter import filedialog


def ler_pdf(caminho_arquivo):
    imagem = pdf2image.convert_from_path(caminho_arquivo)
    for pagenumber, page in enumerate(imagem):
        detect_text = pytesseract.image_to_string(page)
        print(detect_text)

def ler_img(caminho_arquivo):
    detect_text = pytesseract.image_to_string(caminho_arquivo)
    print("In Python what's the corret answer for the following question:\n")
    print(detect_text)
    
if __name__ == '__main__':
    #root = tk.Tk()
    #root.withdraw()
    #caminho_arquivo = filedialog.askopenfilename(filetypes=[('any', '*'),('Pdf', '*.pdf')])
    caminho_arquivo = 'E:/Download/Capture.PNG'
    #ler_pdf(caminho_arquivo)
    ler_img(caminho_arquivo)
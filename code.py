from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import img2pdf
import os

# File name to convert
archivo = 'input.pdf'

# Extract the number of pages that has input.pdf file
pdf = PdfFileReader(open(archivo, 'rb'))
nPages = pdf.getNumPages()

print('Total number of pages to convert: ' + str(nPages))

def main():
  # convert PDF pages to JPG
  for i in range(nPages):
    ii = i + 1
    pages = convert_from_path(archivo, first_page=ii, single_file=True)
    page_name = 'page_' + str(ii) + '.jpg'
    pages[0].save(page_name, quality=100)

  # List of all files *.jpg
  images = [i for i in os.listdir(os.getcwd()) if i.endswith('.jpg')]
  # print(images)

  # Rewrite all the images in the file output.pdf
  with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(images))

if __name__ == "__main__":
  main()

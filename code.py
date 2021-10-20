from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader
import img2pdf
import glob
import os

# Indicate path where the PDF file is located. Use / instead of \ (Windows)
path_pdfs = 'C:/Users/rral/Desktop/pdf2img2pdf/'

# Only the name of the PDF file, Without the extention .pdf
name = 'name_of_pdf_file'

# Change the current working directory
os.chdir(path_pdfs)

# File name to convert
archivo = name + '.pdf'
print('file to convert: ' + archivo)

# Extract the number of pages that has input.pdf file
pdf = PdfFileReader(open(archivo, 'rb'))
nPages = pdf.getNumPages()

print('Total number of pages to convert: ' + str(nPages))

def main():
  # convert PDF pages to JPG
  for i in range(nPages):
    ii = i + 1
    pages = convert_from_path(archivo, first_page=ii, single_file=True)

    # Allows the continuous numbering of the images (01 ... 09)
    if ii < 10:
      ii = '0' + str(ii)

    page_name = 'page_' + str(ii) + '.jpg'
    pages[0].save(page_name, quality=100)

  # List of all files *.jpg
  images = [j for j in os.listdir(os.getcwd()) if j.endswith('.jpg')]

  # Rewrite all the images in the file output.pdf
  with open(name + "_444.pdf", "wb") as k:
    k.write(img2pdf.convert(images))

  # Clean the created images
  for l in glob.glob("Page_*.jpg"):
    os.remove(l)

if __name__ == "__main__":
  main()

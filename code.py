from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader

# File name to convert
archivo = 'input.pdf'

# Extract the number of pages that has input.pdf file
pdf = PdfFileReader(open(archivo, 'rb'))
nPages = pdf.getNumPages()

print('Total number of pages: ' + str(nPages))

def main():
  # convert PDF pages to JPG
  for i in range(nPages):
    ii = i + 1
    pages = convert_from_path(archivo, first_page=ii, single_file=True)
    page_name = 'page_' + str(ii) + '.jpg'
    pages[0].save(page_name, quality=100)

if __name__ == "__main__":
  main()

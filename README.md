# Convert PDF files to img and return to PDF

The purpose of this code is, extract the pages from a PDF file in JPG format.Then, use all the images to restore the new PDF file. In this way, the content of the new PDF will have its content in image format and can not directly copy its content.

For this you use the modules:

* pdf2image
* PyPDF2
* img2pdf
* glob
* os

To execute the code, it only requires modifying two parameters:
  
a) The work directory route in the variable **path_pdfs**. Take into account change the \ by /

```python
path_pdfs = 'C:/Users/rral/Desktop/pdf2img2pdf/'
```
    
b) Indicate only the name of the file without the .pdf extension in the variable **name**
    
```python
name = 'name_of_pdf_file'
```

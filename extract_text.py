import sys
import PyPDF2

pdf_file = str(sys.argv[1])
password = str(sys.argv[2])  
with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    if pdf_reader.is_encrypted:
        if pdf_reader.decrypt(password):
            print(f"Successfully decrypted '{pdf_file}' with the provided password.")
        else:
            print(f"Failed to decrypt '{pdf_file}' with the provided password.")
            exit(1)

    content = {}
    for indx, pdf_page in enumerate(pdf_reader.pages):
        content[indx + 1] = pdf_page.extract_text()

    print(content)



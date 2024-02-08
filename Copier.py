import PyPDF2

def copy_pdf(input_path, output_path):
    # Open the input PDF file
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Copy all pages from the input PDF to the output PDF
        for page in reader.pages:
            writer.add_page(page)

        # Write the copied PDF to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage
input_pdf_path = 'input.pdf'
output_pdf_path = 'output.pdf'
copy_pdf(input_pdf_path, output_pdf_path)

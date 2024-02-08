import PyPDF2

def flatten_pdf(input_path, output_path):
    # Open the PDF file
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Iterate through each page
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)

            # Flatten form fields
            if '/Annots' in page:
                writer_annot = PyPDF2.PdfAnnotationWriter(writer)
                for annotation in page['/Annots']:
                    writer_annot.write(annotation)
                writer_annot.close()

        # Write the flattened PDF to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage
input_pdf_path = 'input.pdf'
output_pdf_path = 'output.pdf'
flatten_pdf(input_pdf_path, output_pdf_path)

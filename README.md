import pdfplumber

def extract_tables_from_pdf(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            tables.extend(page_tables)
    return tables

# Provide the path to your PDF file
pdf_path = 'your_pdf_file.pdf'

# Extract all tables from the PDF
all_tables = extract_tables_from_pdf(pdf_path)

# Process the extracted tables as needed
for table in all_tables:
    for row in table:
        print(row)

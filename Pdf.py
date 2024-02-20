from fpdf import FPDF

def text_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font
    pdf.set_font("Arial", size = 12)
    
    # Read text from input file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    
    # Add text to PDF
    pdf.multi_cell(0, 10, text)
    
    # Save PDF to output file
    pdf.output(output_file)

# Example usage:
input_file = "input.txt"
output_file = "output.pdf"
text_to_pdf(input_file, output_file)

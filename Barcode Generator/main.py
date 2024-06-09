from barcode import EAN13
from barcode.writer import ImageWriter
import re

def generate_barcode():
    # Accept user input for the barcode number
    number = input("Enter a 13-digit EAN-13 barcode number: ")

    # Validate the input
    if not re.match(r'^\d{13}$', number):
        print("Invalid input. Please enter exactly 13 digits.")
        return

    # Accept user input for the file name
    file_name = input("Enter the file name to save the barcode: ")

    # Generate the barcode
    my_code = EAN13(number, writer=ImageWriter())

    # Customize the barcode appearance
    options = {
        'module_width': 0.2,  # Width of each module
        'module_height': 15.0,  # Height of each module
        'font_size': 10,  # Font size for the text
        'text_distance': 1.0,  # Distance between the text and the barcode
        'background': 'white',  # Background color
        'foreground': 'black',  # Foreground color
        'write_text': True,  # Include the text below the barcode
    }

    # Save the barcode
    my_code.save(file_name, options=options)
    print(f"Barcode saved as {file_name}.png")

if __name__ == "__main__":
    generate_barcode()

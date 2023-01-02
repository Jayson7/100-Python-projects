from rembg import remove 
from PIL import Image 


input_path = 'sam.jpg'
output_path = 'sam_no_bg.jpg'

input = Image.open(input_path)
output = remove(input)
output.save(output_path) 
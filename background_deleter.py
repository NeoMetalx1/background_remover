from rembg import remove 
from PIL import Image

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

if __name__ == "__main__":
    input_path = 'D:\\Codes\\Python\\Test\\2024-03-19_211504.png'
    output_path = 'output_image.png'
    remove_background(input_path, output_path)
    print(f'Edited Image Saved in {output_path}')
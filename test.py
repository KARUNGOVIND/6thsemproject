import os
from PIL import Image

def resize_images(input_dir, output_dir, target_size=(150, 150)):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Loop through all files in the input directory
    for filename in files:
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Open the image file
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)

            # Resize the image
            resized_img = img.resize(target_size, Image.ANTIALIAS)

            # Save the resized image to the output directory with the same filename
            output_path = os.path.join(output_dir, filename)
            resized_img.save(output_path)

    print("Image resizing complete.")

# Example usage
input_folder = r'G:\6sem project\Train\non resized\silk'  # Replace 'input_folder' with the path to your input folder
output_folder = r'G:\6sem project\Train\resized\silk'  # Replace 'resized_images' with the path to your output folder
resize_images(input_folder, output_folder)

import os
import shutil

def move_images(source_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Traverse through each subfolder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file is an image (you may want to adjust this condition)
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                # Check if a file with the same name already exists in the destination folder
                if os.path.exists(destination_path):
                    # If yes, rename the file being moved
                    filename, file_extension = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(os.path.join(destination_folder, f"{filename}_{counter}{file_extension}")):
                        counter += 1
                    destination_path = os.path.join(destination_folder, f"{filename}_{counter}{file_extension}")
                # Move the image to the destination folder
                shutil.move(source_path, destination_path)

# Example usage:
source_folder = r'G:\6sem project\dataset\fabrics\Fabrics\Cotton'
destination_folder = r'G:\6sem project\Train\cotton'
move_images(source_folder, destination_folder)

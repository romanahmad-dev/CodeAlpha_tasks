# -*- coding: utf-8 -*-
"""Task Automation with Python Scripts.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cw0oFLHtyGpUivcdGju3fpHUXDz267_X
"""

# Step 1: Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')

# Step 2: Import required libraries
import os
import shutil

# Step 3: Define the directory to organize (change this to your downloads path in Google Drive)
downloads_folder = 'https://drive.google.com/drive/folders/1U98lM6kdDg80zNlH3htmZYxAYe6MU3KG?usp=drive_link'  # Replace with your actual folder path

# Step 4: Define folders for different file types
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Others': []  # For files that do not match any type
}

# Step 5: Create folders if they don't exist
for folder in folders:
    os.makedirs(os.path.join(downloads_folder, folder), exist_ok=True)

# Step 6: Move files into corresponding folders
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):  # Check if it's a file
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in folders.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(downloads_folder, folder, filename))
                moved = True
                print(f'Moved: {filename} to {folder}')
                break

        if not moved:
            # Move to 'Others' if file type is not recognized
            shutil.move(file_path, os.path.join(downloads_folder, 'Others', filename))
            print(f'Moved: {filename} to Others')

print("File organization complete!")
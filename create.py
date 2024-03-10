import os
import random
import string

# Function to create files with given extension and content
def create_files(extension, content):
    for i in range(10):
        with open(f"{extension}_file_{i}.{extension}", "w") as file:
            file.write(content)

# Create 10 files with different extensions and content
create_files("pdf", "Welcome to the world of Python")
create_files("txt", "This is a text file.")
create_files("jpg", "This is a JPG image.")
create_files("png", "This is a PNG image.")
import os
import shutil
import time 

response = {}

def sort_files():
    # Get the current working directory
    current_directory = os.getcwd()

    # Iterate through all files in the current directory
    files = os.listdir(current_directory)
    for file in files:
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(current_directory, file)):
            # Check if the file has an extension
            file_name, file_extension = os.path.splitext(file)
            dir_name = f"SORT {file_extension[1:].upper()}" 

            # Skip files without extension or Python files
            if file_extension == "" or file_extension == ".py": 
                continue
            
            # Specify the directory to move files
            target_directory = os.path.join(current_directory, dir_name)
            os.makedirs(target_directory, exist_ok=True)
            
            # Construct the full path to the source file
            source_file = os.path.join(current_directory, file)
            # Construct the destination path
            destination_file = os.path.join(target_directory, file)

            # Move the file to the specified directory
            shutil.move(source_file, destination_file)
            response[dir_name] = response.get(dir_name, 0) + 1

def output_changes():
    if response == {}:
        print("No files were moved.")
        return
    for dir_name, count in response.items():
        print(f"{dir_name} moved {count} file(s)")

def main():
    sort_files()
    output_changes()

if __name__ == "__main__":
    main()

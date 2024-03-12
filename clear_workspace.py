import os
import shutil

def clear_workspace():
    current_directory = os.getcwd()
    for item in os.listdir(current_directory):
        print(item)
        if item == ".git":
            continue
        item_path = os.path.join(current_directory, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"Deleted {item_path}")

    print("Workspace cleared")

def main():
    clear_workspace()

if __name__ == "__main__":
    main()

import os
import shutil

def organize_files(directory):
    """Organize files in the specified directory by their extensions."""
    # Change the working directory
    os.chdir(directory)

    # Iterate over all the files in the directory
    for filename in os.listdir('.'):
        # Skip directories
        if os.path.isdir(filename):
            continue
        
        # Get the file extension
        _, ext = os.path.splitext(filename)
        
        # Create a new directory for the extension if it doesn't exist
        if ext:
            ext_dir = ext[1:]  # Remove the leading dot
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)

            # Move the file into the corresponding directory
            shutil.move(filename, os.path.join(ext_dir, filename))
            print(f'Moved: {filename} -> {ext_dir}/{filename}')

def main():
    # Get the directory to organize from the user
    directory = input("Enter the path of the directory to organize: ")
    
    if os.path.exists(directory) and os.path.isdir(directory):
        organize_files(directory)
        print("Files organized successfully!")
    else:
        print("Invalid directory. Please check the path and try again.")

if __name__ == "__main__":
    main()

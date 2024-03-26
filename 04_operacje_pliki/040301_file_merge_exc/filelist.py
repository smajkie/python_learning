import os

def list_files_in_directory(directory):
    """Lists all files in the given directory."""
    try:
        # List all entries in the directory
        entries = os.listdir(directory)
        # Filter out entries that are files
        files = [file for file in entries if os.path.isfile(os.path.join(directory, file))]
        return files
    except FileNotFoundError:
        print(f"The directory {directory} was not found.")
    except NotADirectoryError:
        print(f"{directory} is not a directory.")
    except PermissionError:
        print(f"Permission denied to access {directory}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'your_directory_path' with the actual directory path you want to list files from.
if __name__ == '__main__':
    files = list_files_in_directory('your_directory_path')
    for file in files:
        print(file)
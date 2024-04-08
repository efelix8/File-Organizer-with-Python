import os
import mimetypes
import json
from pathlib import Path
from tqdm import tqdm
from argparse import ArgumentParser
from logging import basicConfig, INFO

# Folder Definitions
folders = {
    "Programming Files": {"ipynb", "py", "java", "cs", "js", "vsix", "jar", "cc", "ccc", "html", "xml", "kt"},
    "Music": {"mp3", "wav", "wma", "mpa", "ram", "ra", "aac", "aif", "m4a", "tsa"},
    "Videos": {"mp4", "webm", "mkv", "MPG", "MP2", "MPEG", "MPE", "MPV", "OGG", "M4P", "M4V", "WMV", "MOV", "QT", "FLV", "SWF", "AVCHD", "avi", "mpg", "mpe", "mpeg", "asf", "wmv", "mov", "qt", "rm"},
    "Pictures": {"png", "jpg", "jpeg", "gif", "tiff", "raw", "webp", "jfif", "ico", "psd", "svg", "ai"},
    "Applications": {"exe", "msi", "deb", "rpm"},
    "Compressed": {"zip", "rar", "arj", "gz", "sit", "sitx", "sea", "ace", "bz2", "7z"},
    "Documents": {"txt", "pdf", "doc", "xlsx", "pdf", "ppt", "pps", "docx", "pptx"},
    "Other": {},
}

# Functions
def create_folders(folder_name):
    """Creates the specified folder and checks its existence."""
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"{folder_name:20} {'' if os.path.exists(folder_name) else 'Created'}")
    except OSError as e:
        print(f"Error: Folder {folder_name} could not be created: {e}")

def get_folder(file_name):
    """Returns the folder name based on the file extension."""
    mimetype, _ = mimetypes.guess_type(file_name)
    if mimetype is None:
        return "Other"
    main_type = mimetype.split("/")[0]
    return folders.get(main_type, "Other")

def move_file(file_name, folder_name):
    """Moves the file to the specified folder and handles errors."""
    try:
        os.rename(file_name, os.path.join(folder_name, file_name))
        return True
    except OSError as e:
        print(f"Error: File {file_name} could not be moved: {e}")
        return False

def start(folder_path):
    """Categorizes and moves files in the specified folder."""
    folder_path = Path(folder_path)
    for file_path in tqdm(folder_path.glob("*")):
        if file_path.name != __file__ and not file_path.name.startswith('.'):
            ext = file_path.suffix.lower()
            if ext:
                folder = get_folder(file_path)
                dest_folder = folder_path / folder
                create_folders(dest_folder)
                if not dest_folder.exists() or not file_path.is_file():
                    move_file(str(file_path), str(dest_folder))

# Main Function
if __name__ == "__main__":
    # Parse command line arguments
    parser = ArgumentParser()
    parser.add_argument('-d', '--directory', help='The directory to scan for files')
    args = parser.parse_args()

    # Get the directory path
    if args.directory is None:
        print("Error: Directory input is required.")
        exit()

    # Start the file organization process
    start(args.directory)

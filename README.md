# File-Organizer-with-Python
This Python script automates file organization by categorizing them by file extensions and moving them to predefined folders.

**Features:**

- Supports various file types: Programming, Music, Videos, Pictures, Applications, Compressed, Documents, and Other (catch-all).
- Handles unknown file types by placing them in the "Other" folder.
- Provides progress indication using a tqdm progress bar.
- Creates missing folders as needed.
- Silently ignores hidden files and the script itself (`file_organizer.py`).

**Installation**

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/your-username/file-organizer.git
   ```
   or download the `file_organizer.py` script.

2. Install required dependencies (if not already installed):
   ```bash
   pip install tqdm
   ```

**Usage**

1. Run the script from the command line, specifying the directory to organize:
   ```bash
   python file_organizer.py -d /path/to/your/directory
   ```
   Replace `/path/to/your/directory` with the actual path to the directory you want to organize.

2. The script will scan the directory, categorize files, create missing folders, and move files to their respective locations.

**Example**

```
python file_organizer.py -d /home/user/Downloads
```

This will organize files in the `/home/user/Downloads` directory.

**Customization**

- You can modify the `folders` dictionary in the script to add or remove categories.
- Adjust folder names to suit your preferences.

**Logging (Optional)**

- Uncomment the `basicConfig` line at the beginning of the script to enable logging messages (INFO level by default).
- You can modify the logging level as needed.

**Contributing**

We welcome contributions to improve this script. Feel free to submit pull requests!

**License**

This project is licensed under the MIT License (see LICENSE file for details).

**Enjoy a more organized file system!**

**Additional Considerations:**

- Error handling: While the script includes basic error handling for file movement, consider adding more comprehensive checks for potential issues (e.g., insufficient permissions, disk space limitations).
- Advanced configuration: Explore options for allowing users to specify custom folder locations or file type mappings via configuration files or command-line arguments.
- Testing: Implement unit tests to ensure the script's functionality and catch regressions in future modifications.

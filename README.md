# Automated File Organization Script

This project is a Python script that automates the process of organizing files in a directory based on their file extension. The script creates subdirectories for different file types (images, codes, videos, docs, and apps) and moves files to their appropriate directories based on their extension.

The script utilizes Python's built-in `os` and `shutil` modules to automate the file management process, reducing the need for manual file organization. It also includes error handling to prevent file overwrite errors by checking if the target subdirectories already exist before creating them.

## Getting Started

To use this script, simply place it in the directory you want to organize and run it using the command `python organize_directory.py` in your terminal. The script will automatically create subdirectories for each file type and move the files to their appropriate directory based on their extension.

## Supported File Types

The script currently supports the following file types:

- Images: .png, .jpg, .gif, .jpeg
- Codes: .py, .css, .html, .bash
- Videos: .mp4, .wav, .webm
- Docs: .pdf, .doc, .txt
- Apps: .dmg, .exe

## Contributing

If you find any bugs or have suggestions for improving the script, please feel free to submit an issue or pull request on GitHub.

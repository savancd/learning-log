

# 🗂️ Image Sorter GUI App (Python) - Documentation

## 📦 Purpose

A Python GUI app that:
- Recursively scans a selected folder (and subfolders) for image files
- Sorts images into subfolders by **creation date** (EXIF or file system)
- Allows user to choose source and destination directories
- Preserves original filenames
- Does **not overwrite** existing files
- Does **not delete** originals

---

## ✅ Requirements

- Python 3
- Tkinter (included in most Python installs)
- Pillow (for reading image EXIF metadata)

### 📥 Install Pillow:

```bash
pip3 install Pillow

🚀 How to Run

    Save the script as image_sorter_gui.py

    Run it in a terminal within your GUI desktop environment:

python3 image_sorter_gui.py

    Use the GUI:

        Select a source folder

        Select a destination folder

        Click Sort Images

🔐 Safe Behavior

    Files are copied, not moved.

    Folders are created as YYYY-MM-DD based on:

        EXIF DateTimeOriginal (for images)

        File creation date (if no EXIF)

    Files with the same name are not overwritten — they are skipped.

    Original folders are untouched — you can delete them manually after review.

🖼️ Supported Image Extensions (default)

('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif', '.heic', '.raw', 'dng')

You can add more as needed.
📁 Adding Support for Videos and Documents

You can sort videos or documents by simply changing the file extensions list.
🎥 Video Extensions:

('.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv')

📄 Document Extensions:

('.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.odt')

    🧠 These file types don’t have EXIF, so the script will fall back to os.path.getctime() for file creation time.

🖥️ Creating a Desktop Launcher

    Create image_sorter_gui.desktop:

[Desktop Entry]
Type=Application
Name=Image Sorter GUI
Comment=Sort images by date with a GUI
Exec=python3 /home/YOURUSERNAME/Desktop/image_sorter_gui.py
Icon=folder-pictures
Terminal=false
Categories=Utility;Graphics;
StartupNotify=true

    Make it executable:

chmod +x ~/Desktop/image_sorter_gui.desktop

    Double-click from your Desktop.

    If prompted to trust the launcher, approve it.

🧠 Future Improvements

    Auto-rename duplicates (file_1.jpg, etc.)

    Option to move instead of copy

    Advanced date extraction for videos (ffprobe)

    Sort documents by content (advanced OCR/timestamps)

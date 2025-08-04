# 📂 Folder Organizer (Python Script)

Hi! I'm currently learning Python and working on automating small tasks to get better at file handling, working with JSON, and using built-in modules like `os` and `shutil`.

This script is a basic **folder organizer** that sorts files in a selected directory based on their file type (like images, documents, videos, etc.).

## 🧠 What I Learned

- How to read and parse a `.json` config file
- Looping through files in a directory using `os.listdir()`
- Splitting file names and extensions with `os.path.splitext()`
- Moving files with `shutil.move()`
- Creating folders automatically with `os.makedirs()`

## 🛠 How It Works

1. The script asks you for a folder path.
2. It checks each file inside that folder.
3. Based on the file extension, it moves the file into a category folder like `Images`, `Docs`, `Scripts`, etc.
4. The categories are stored in a JSON config file called `config.json`.

## 📝 Example Categories (from `config.json`)

```json
{
  "Images": [".jpg", ".jpeg", ".png"],
  "Docs": [".pdf", ".docx", ".txt"],
  "Video": [".mp4", ".mov"],
  "Scripts": [".py", ".sh"]
}


🚧 Notes / To-Do
Add error handling (e.g. if the folder doesn’t exist)

Let users customize categories from the script

Possibly build a GUI for easier use in the future

🔍 Why I Made This
I'm a CS student / self-taught dev just trying to get more comfortable with Python by solving real problems—even if they're small. This was a great way to practice and see how modules like os and shutil can automate stuff I do manually every day.

Thanks for checking it out! ✌️
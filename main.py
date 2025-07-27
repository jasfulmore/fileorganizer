import os
import shutil
import json

# asking for user input (files)
folder_input = input("What folder would you like to organize?: \n")

# open and laod w type configs from JSON file
with open('config.json', 'r') as f:
    file_types = json.load(f)

# optional: defines each type of file if JSON fails or unused
file_types = {
    'Images': ['.jpg', '.png', '.jpeg'],
    'Docs': ['.pdf', '.docx', '.txt'],
    'Video': ['.mp4', '.mov'],
    'Scripts': ['.py', '.sh'] 
}

# looping through every file in the folder given by user
for filename in os.listdir(folder_input):
    file_path = os.path.join(folder_input, filename)

    # checking that the file is indeed a file
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        moved = False


        # check if file extension matches any defined catagory
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_input, folder)
                os.makedirs(target_folder, exist_ok=True)  # create folder if it doesn't exist
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} → {folder}")
                moved = True
                break
    
            # Move the file into the category folder
            shutil.move(file_path, os.path.join(folder_input, filename))
            print(f"Moved {filename} → {folder}")
            moved = True
            break    

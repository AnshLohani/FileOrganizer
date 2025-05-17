import os 
import shutil 

# === File types to be sorted out ===
FILE_TYPES = {
    "Images": ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Code": ['.py', '.js', '.cpp', '.java', '.html', '.css'],
    "Others": []
}

# === Get Extention Category ===
def getCategory(extention):
    for category,extentions in FILE_TYPES.items():
        if extention.lower() in extentions:
            return category
    return "Others"

# === Path of the Subject Folder ===
DIR = input("Enter the path to the folder you want to organize: ").strip()
if not os.path.isdir(DIR):
    print("Invalid path. Please check again.")
    exit()

# === Main Organizing Function === 
for filename in os.listdir(DIR):
    filepath = os.path.join(DIR,filename)

    if os.path.isfile(filepath): # Checks if the object we are on is a file or not (it skips the folders)
        _, ext = os.path.splitext(filename) # Spliting the Name and the Extention of the given file
        category = getCategory(extention=ext)
        category_folder = os.path.join(DIR,category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        shutil.move(filepath,os.path.join(category_folder,filename))
        print(f"Moved {filename} ---> {category} \n")
    
    else:
        pass
import os
import shutil
import inotify.adapters

downloads_path = os.environ["HOME"] + '/Downloads'

folder_association = {
        ".jpg": "media",
        ".png": "media",
        ".ico": "media",
        ".mp4": "media",
        ".xcf": "media",
        ".pdf": "docs",
        ".xls": "docs",
        ".csv": "docs",
        ".doc": "docs",
        ".docx": "docs",
        ".txt": "docs",
        ".xml": "docs",
        ".md": "docs",
        ".ppt": "docs",
        ".xps": "docs",
        ".md": "docs",
        ".iso": "distribution_image",
        ".html": "web",
        ".css": "web",
        ".js": "web",
        ".php": "web",
        ".py": "script",
        ".sh": "script",
        ".zip": "compressed",
        ".tar": "compressed",
        ".zip": "compressed",
        ".7z": "compressed",
        ".GZ": "compressed",
        ".rar": "compressed",
        ".bak": "backup"
        }

def main():
    create_folders()

    initial_clean()

    i = inotify.adapters.Inotify()

    i.add_watch(downloads_path)

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print(type_names)
        if type_names[0] != "IN_CREATE":
            continue

        clean_file(filename, path)

def clean_file(filename, path):
    try:
        dot_index = filename.index(".")
        extension = filename[dot_index:]

        try:
            folder = folder_association[extension] 
        except:
            folder = "misc"

    except:
        extension = "none"
        folder = "misc"

    file_full_path = path + "/" + filename
    new_file_full_path = path + "/" + folder + "/"+ filename

    print(file_full_path, new_file_full_path)

    shutil.move(file_full_path, new_file_full_path)
    print(extension, folder)

def create_folders():
    def get_unique_folders():
        unique_folders = []
        for folder_key  in folder_association.keys():
            if folder_association[folder_key] not in unique_folders:
                unique_folders.append(folder_association[folder_key])
        return unique_folders

    unique_folders = get_unique_folders()

    print(unique_folders)
    for folder in unique_folders:
        try:
            os.mkdir(downloads_path + "/" + folder)
        except:
            print("Folder " + folder + " already exists")

    return False

def initial_clean():
    files = []
    for (dirpath, dirnames, filenames) in os.walk(downloads_path):
        files.extend(filenames)
        break
    print(files)

    for filename in files:
        clean_file(filename, downloads_path)


if __name__ == "__main__":
    main()

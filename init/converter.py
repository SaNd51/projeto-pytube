import os, re, shutil

def rename_file(file):
    file_name, file_extension = os.path.splitext(file)       
    if not file_name:
        return file
    file_extension = '.mp3'

    return f'{file_name}{file_extension}'
 
def file_loop(root, files):
    for file in files:
        if not re.search(r'\.mp4$', file):
            continue

        new_file_name = rename_file(file)
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)
        shutil.move(old_file_full_path, new_file_full_path)
    
def main_loop():
    main_folder = os.getcwd()
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, files)


      
      
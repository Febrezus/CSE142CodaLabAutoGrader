import os
import re
import shutil
import zipfile

submission_re = r"(.*?) - \d+ (.+?\..*)"

def main():
    # get the current directory
    path = os.getcwd()

    for filename in os.listdir(path):
        # split the filename into name, number, and type
        match = re.search(submission_re, filename)
        # print(parts)
        if match:
            name, file_type = match.group(1), match.group(2)
            new_dir = os.path.join(path, name)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            # if the file is a zip file, unzip it
            if file_type.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(path, filename), 'r') as zip_ref:
                    zip_ref.extractall(new_dir)
            shutil.move(os.path.join(path, filename), os.path.join(new_dir, filename))

if __name__ == "__main__":
   main()

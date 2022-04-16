import os


path = 'C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\naildystrophy\\'
# path = 'C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\onychomycosis\\'


files = os.listdir(path)
for each_file in files:
    old_full_path = "%s\\%s" % (path, each_file)
    new_full_path = "%s\\%s" % (
        path, each_file.replace('resized', ''))
    # Absolute path of a file
    old_name = old_full_path
    new_name = new_full_path

    # Renaming the file
    os.rename(old_name, new_name)

print('Done')

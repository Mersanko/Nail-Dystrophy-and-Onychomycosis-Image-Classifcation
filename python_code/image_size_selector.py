import os

path = 'C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\naildystrophy\\'
# path = 'C:\\Users\\Admin\\OneDrive - g.msuiit.edu.ph\\Desktop\\pythonprojectofmylife\\datasets (B1, B2, C, D, E)\\B1\\onychomycosis\\'

resized_image_indicator = 'resized'

files = os.listdir(path)
for each_file in files:
    full_path = "%s\\%s" % (path, each_file)
    if resized_image_indicator in each_file:
        continue
    else:
        os.unlink(full_path)
print('Done')

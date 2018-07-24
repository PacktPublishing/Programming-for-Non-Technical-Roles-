import os
import shutil

directory = os.chdir("/Users/guillermovalleschavez/Downloads")

files = os.listdir(directory)


# identify the destination path for each folder type

# show terminal

dest1 = "/Users/guillermovalleschavez/Downloads/PDF Files"
dest2 = "/Users/guillermovalleschavez/Downloads/JPEG Images"
dest3 = "/Users/guillermovalleschavez/Downloads/Powerpoint files"

# Now let's make the magic happen by moving file per type in their respective folder
for file in files:
    if file.endswith('.pdf'):
        shutil.move (file, dest1)
    elif file.endswith('.PDF'):
        shutil.move (file, dest1)
    elif file.endswith('.jpeg'):
        shutil.move (file, dest2)
    elif file.endswith('.pptx'):
        shutil.move (file, dest3)











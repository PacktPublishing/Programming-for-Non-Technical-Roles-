import os


# changing the directory
directory = os.chdir("/Users/guillermovalleschavez/Downloads")

files = os.listdir(directory)

# printing the directory

# print(files)

#creating the folders for the files to go into

for file in files:
    if file.endswith(".pdf"):
        os.mkdir("PDF Files")
        break

for file in files:
    if file.endswith(".jpeg"):
        os.mkdir("JPEG Images")
        break

for file in files:
    if file.endswith(".pptx"):
        os.mkdir("Powerpoint files")
        break



# pdf_files = [f for f in files if f.endswith(".epub")]
# os.mkdir("EPUB")



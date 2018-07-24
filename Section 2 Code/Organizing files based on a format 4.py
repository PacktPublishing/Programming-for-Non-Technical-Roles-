import os


directory = os.chdir("/Users/guillermovalleschavez/Desktop/python/course_files /March NOAs")


files = os.listdir(directory)

# print(files)

# format we want 25 company_name structure.extension

# loop through the list

# remove temporary files if needed
# os.remove(".DS_Store")


for file in files:
    # get tuple separate it

    # print(os.path.splitext(file))

    # divide the files into the name and extension of the list
    file_name, extension = os.path.splitext(file)

     # split into the categories

    # print(file_name.split("-"))

    company_name, structure, date = file_name.split("-")

    # print(structure)

    structure = structure.strip()[:8]

    # print(structure)


    date = date.strip()[6:8]

    # print(date)


    # add a zero so that the files are properly ordered

    proper_date = date.zfill(2)

    # print(proper_date)



    new_name = "{} {}- {}{}".format(proper_date, company_name, structure, extension)

    # print(new_name)

    os.rename(file, new_name)

# import the filecmp module
import filecmp

# create a list of file names
files = ["database.txt", "database1.txt", "database2.txt", "database3.txt", "database4.txt", "database5.txt", "database6.txt", "database7.txt", "database8.txt", "database9.txt", "database10.txt"]

# compare each file with the first one
for file in files[1:]:
    # use filecmp.cmp() to compare the contents of the files
    if not filecmp.cmp(files[0], file):
        # print the name of the file that is different
        print(f"{file} is different from {files[0]}")

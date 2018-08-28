import os

# open file for reading
abs_file_path = 'c:/varun/python/test1/file1.txt'
f = open(abs_file_path,'r')
print(f.readlines())
f.close()


#opening a file using 'with' statements require no explicit closing of file
with open(abs_file_path,'r') as f_in:
    # read the whole file and print... not a good idea if file is huge
    print(f_in.read())
    # read file line by line
    for line in f_in:
        print(line)
#get the current directory
current_directory = os.getcwd()

#list all the files in that directory 
os.listdir(current_directory)

#rename the files in that directory
os.rename(original_name, new_name)

for i in files:
    file_name = i.replace("_(Solution)", "")
    os.rename(i,file_name)

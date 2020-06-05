#get the current directory
current_directory = os.getcwd()

#list all the files in that directory 
os.listdir(current_directory)

#rename the files in that directory
os.rename(original_name, new_name)

for i in files:
    file_name = i.replace("_(Solution)", "")
    os.rename(i,file_name)

#find similarity between the strings
#this gives the percentage of similarity between the strings, if the similarity is more than 0.5 it prints the other string

from difflib import SequenceMatcher
name = "karlanthony-towns"
sname = ['karl-anthony-towns']
name = [sname for sname in special_names if SequenceMatcher(None, name,sname).ratio()>0.5][0]
>>> name
'karl-anthony-towns'

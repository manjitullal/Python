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

#one way to time your code
import timeit
start = timeit.default_timer()
#code
end = timeit.default_timer() - start

#convert characters with ticks like german characters with no ticks
import unidecode
>>> name = "Mesut Özil"
>>> player = unidecode.unidecode(name)
>>> player
'Mesut Ozil'

#load kaggle dataset
#https://www.kaggle.com/general/74235

#make sure that you have the kaggle.json file store in your colab before doing below

from google.colab import drive
drive.mount('/content/drive')

! mkdir ~/.kaggle
! cp /content/drive/MyDrive/datasets/kaggle/kaggle.json ~/.kaggle/
! kaggle datasets download -d tmdb/tmdb-movie-metadata
! unzip tmdb-movie-metadata.zip -d tmdb-movie-metadata

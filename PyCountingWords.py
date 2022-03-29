#for arabic input use a pre-cleaned pre-formatted input directly
#removing tashkeel/harakat may take sometime to develop
#tnkeeh library was not useful in my case I found alternative quicklier
#please uncomment the first two lines if you want to try tnkeeh lib
#import tnkeeh as tn
#tn.clean_data(file_path = 'kalemat.txt', save_path = 'cleaned_data.txt',)

#opens a text file (in the same dir), read 
with open('kalemat.txt', 'r') as file:
    input_string = file.read().rstrip()
    string =input_string.split(" ")

word_list = input_string.split()
new = []

#adds only words to the list, ensures no repition
for word in word_list:
    if word.isalpha() == False:
        new.append(word[:-1])
    else:
        new.append(word)

from collections import Counter

print("="*65)   

print(Counter(new))

print("*"*65)   

#create csv file with output in proper format using pandas library - in the same dir
import pandas as pd
pd.DataFrame(Counter(new).most_common(), columns=["item", "count"]).to_csv("./myfile.csv")




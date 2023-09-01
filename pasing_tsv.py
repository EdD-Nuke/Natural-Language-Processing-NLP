import csv
from nltk.tokenize import word_tokenize
import re

def read_file(filename): 
    with open(filename, 'r') as file:
         text = file.read() 
    return text

text = read_file("nlmaps.tsv")
words = word_tokenize(text)

if re.search("^fire brigades", "Paris"):
    print("Found!!!")

    
# def read_file(filename): 
#     with open(filename, 'r') as file:
#          text = file.read() 
#     return text

# ans = []
 
# # open .tsv file
# with open("nlmaps.tsv") as f:
   
#   # Read data line by line
#   for line in f:
     
#     # split data by tab
#     # store it in list
#     l=line.split('\t')
     
#     # append list to ans
#     ans.append(l)
 
# # print data line by line
# for i in ans:
#     print(i)

# for k in ans:
#     j = line.split()

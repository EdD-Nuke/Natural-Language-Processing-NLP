from nltk.tokenize import word_tokenize, sent_tokenize
import re
from pprint import pprint


filename = 'nlmaps.tsv'
def red ():
    word = input("Enter: ")
    word2 = input("Enter: ")
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            if word & word2 in line:
                print(line)

red()
# with open('nlmaps.tsv', 'r') as file:
#     reg_f = file.read()
#     scene_one = re.split('SCENE 2:', reg_f)[0]
# # Split scene_one into sentences: sentences
# sentences = sent_tokenize(scene_one)

# # Use word_tokenize to tokenize the fourth sentence: tokenized_sent
# tokenized_sent = word_tokenize(sentences[3])

# # Make a set of unique tokens in the entire scene: unique_tokens
# unique_tokens = set(word_tokenize(scene_one))

# print(unique_tokens)

# poi = input("Enter poi: ")
# loc = input("Enter loc: ")
# while True:
#     file = open('nlmaps.tsv', 'r')
#     if poi & loc in sentences:
#         print('%s: %s is present in" + return sentence both poi and loc' % (poi, loc))
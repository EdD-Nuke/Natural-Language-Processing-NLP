import nltk
import csv
from nltk.tokenize import word_tokenize
import re
from nltk.tokenize import RegexpTokenizer
import sys
from nltk.tokenize import sent_tokenize
from pprint import pprint

regex_tokenizer = RegexpTokenizer('\?', gaps = True)
def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
    return entity_names

    
with open('nlmaps.tsv', 'rt') as f:
    for line in f:
        sentences = nltk.sent_tokenize(line)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

        entities = []
        for tree in chunked_sentences:
            entities.extend(extract_entity_names(tree))

        print(entities)


# p = re.compile(r"(\w+)\s(?:(wa |" + entities + "|)", re.VERBOSE)
# l = re.compiler(r"")
# for words in l:
#     print p.search(words).expand(r"\g<1> <-- the code is --> \g<2>")
# #re.search('keyval('','')) + nwr(keyval('','')), keyval('','')) + nwr(keyval('','')))

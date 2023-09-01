import nltk
from typing import Counter
from nltk.corpus import treebank
from nltk import PCFG

frequencies = dict()
for tree in treebank.parsed_sents()[:100]:
    # binary format:
    tree.chomsky_normal_form() #always start with n non terminal
    productions = tree.productions()
    alpha_beta = 0 #left
    counter_alpha_beta = Counter()
    for alpha_beta in productions:
        lhs = alpha_beta.lhs()
        rhs = alpha_beta.rhs()
        counter_beta = Counter()
        counter_beta[rhs]
        counter_alpha_beta[alpha_beta]
    #   alpha = alpha_beta.lhs()
    #   updat

for beta in productions:

# build probabilities.
# build grammar. PRobabilisticPRoduction (alpha och beta och prob)
def __init__(self, lhs, rhs, **prob):
    
# test on first 5 sentences of the treebank:
# treebank.sents()[:5]

# for each alpha_beta production:
#     #   alpha = alpha_beta.lhs()
#     # update

# # build probabilities.
# # build grammar.
# # test on first 5 sentences of the treebank:
# # treebank.sents()[:5]

# #For the last part:
# viterbi_parser = nltk.ViterbiParser(grammar)
# for tree in viterbi_parser.parse(['Jack', 'saw', 'telescope']):
#     print (tree)

from typing import Counter
import nltk
from nltk.corpus import treebank
from nltk.parse import ViterbiParser
from nltk.grammar import ProbabilisticProduction
from nltk import Nonterminal
from nltk import PCFG
from nltk import grammar

def count_alpha_betas():
    alpha_counter = Counter()
    alpha_beta_counters = dict()

    for tree in treebank.parsed_sents()[:100]:
        tree.chomsky_normal_form()
        
        productions = tree.productions()

        for alpha_beta in productions:
            alpha = alpha_beta.lhs()
            
            alpha_beta_counter = alpha_beta_counters.setdefault(alpha, Counter())
            betas = alpha_beta.rhs()

            alpha_counter[alpha] += 1
            alpha_beta_counter[betas] += 1

    return alpha_counter, alpha_beta_counters


def counts_to_probabilities(alpha_counter, alpha_beta_counters):
    probabilities = dict()

    for alpha in alpha_counter:
        key_total_count = alpha_counter[alpha]

        beta_probabilities = dict()
        for beta in alpha_beta_counters[alpha]:
            p = alpha_beta_counters[alpha][beta] / key_total_count
            beta_probabilities[beta] = p

        probabilities[alpha] = beta_probabilities
    return probabilities

def probabilities_to_productions(alpha_beta_probabilities):
    rules = []
    for alpha in alpha_beta_probabilities:
        for beta in alpha_beta_probabilities[alpha]:
            probability = alpha_beta_probabilities[alpha][beta]
            al_be_rules = ProbabilisticProduction(alpha, beta, prob=probability)
            rules.append(al_be_rules)
    return rules

def probabilities_to_grammar(productions):
    start = Nonterminal('S')
    grammar = PCFG(start, productions)
    return grammar

alpha_counter, alpha_beta_counters = count_alpha_betas()
alpha_beta_probabilities = counts_to_probabilities(alpha_counter, alpha_beta_counters)
rules = probabilities_to_productions(alpha_beta_probabilities)
grammar = probabilities_to_grammar(rules)

for sentences in treebank.sents()[:5]:
    viterbi_parser = ViterbiParser(grammar)
    for tree in viterbi_parser.parse(sentences):
        print (tree)
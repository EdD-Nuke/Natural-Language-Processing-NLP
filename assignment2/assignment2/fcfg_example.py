from nltk import grammar, parse

g = grammar.FeatureGrammar.fromstring("""
## Non-terminals
# Sentence:
S -> NP VP

# Verb Phrase
VP -> IVerb
VP -> TVerb NP
VP -> TVerb NP PP

# Noun Phrase
NP -> Det Nom
NP -> Det Nom PP
NP -> PropN

# Prepositional Phrase
PP -> P NP

## Terminals a.k.a. Lexicon
# Verbs
IVerb[tense='past'] -> 'walked'
TVerb[tense='past'] -> 'saw' | 'ate'
TVerb[tense='pres', num='pl'] -> 'see'
TVerb[tense='pres', num='sg'] -> 'sees'

# Determiners
Det -> 'the' | 'a'

## Nominals
Nom[phon='c'] -> 'dog' | 'man' | 'garden' | 'grass' | 'lunatic'
Nom[phon='v'] -> 'apple'
PropN[num='sg'] -> 'Mehdi'

# Preposition
P[loc='in'] -> 'in'
P[loc='on'] -> 'on'

""")

parser = parse.FeatureEarleyChartParser(g)

## Modify the grammar above to account for grammatical/ungrammatical sentences
sentences = [
    # grammatical
    "Mehdi walked in the garden",
    "Mehdi sees the lunatic on the grass",
    "a dog chased a cat",
    "a lunatic ate an apple",
    # ungrammatical
    "Mehdi see the lunatic in the garden",
    "Mehdi saw the lunatic in the grass",
    "a dog chase a cat",
    "a lunatic ate a apple",
]

for raw in sentences:
    print("====")
    print(raw)
    sentence = raw.split()  # tokenize
    trees = parser.parse(sentence)
    count = 0
    for tree in trees:
        count += 1
        print(count, tree)
        #tree.draw()
        print("----")
    if count == 0:
        # there shouldn't be any parse tree for ungrammatical sentences.
        print('THERE IS NO PARSE TREE!')

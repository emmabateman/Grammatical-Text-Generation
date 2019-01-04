import random
import re
import sys

import nltk
from nltk import grammar

def main():
    #Load and sort grammar.
    grammar = nltk.data.load(sys.argv[1])
    grammar_dict = {}
    for production in grammar.productions():
        nt = production.lhs().symbol()
        if nt in grammar_dict:
            grammar_dict[nt].append(production.rhs())
        else:
            grammar_dict[nt] = [production.rhs()]

    #Generate sentence from start symbol.
    print(generate(grammar.start().symbol(), grammar_dict))
    
#Recursively generate a string of terminals from a nonterminal symbol
def generate(symbol, grammar_dict):
    if symbol in grammar_dict:
        output = [] 
        rule = random.choice(grammar_dict[symbol])
        for element in rule:
            if grammar.is_nonterminal(element):
                output.append(generate(element.symbol(), grammar_dict))
            else:
                output.append(element)
        return ' '.join(output)
    return symbol

main()

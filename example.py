from Markov import MarkovChain
from Instances import CharMarkovChain, WordMarkovChain

with open("richard3.txt") as f:
    data = f.read()

    mc = WordMarkovChain(data)
    mc.set_order(3)
    print "100 word order-3 Markov chain, by word:\n"
    print mc.chain(100).lower()
    print "\n"

    mc2 = CharMarkovChain(data.replace("\n", " "))
    mc2.set_order(2)
    print "500 character order-2 Markov chain, by character:\n"
    print mc2.chain(500)

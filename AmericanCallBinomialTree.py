
from binomial.StockBinomialTree import AmericanCallBinomialTree
from binomial2 import bintree

if __name__ == '__main__':
    amCall = AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall.getPrice()

    amCall2 = bintree.AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall2.getPrice()
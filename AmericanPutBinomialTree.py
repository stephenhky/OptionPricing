
from binomial.StockBinomialTree import AmericanPutBinomialTree
from binomial2 import bintree

if __name__ == '__main__':
    amPut = AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut.getPrice()

    amPut2 = bintree.AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut2.getPrice()
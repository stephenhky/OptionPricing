
from binomial.StockBinomialTree import EuropeanPutBinomialTree
from binomial2 import bintree

if __name__ == '__main__':
    euroPut = EuropeanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print euroPut.getPrice()

    euroPut2 = bintree.EuropeanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print euroPut2.getPrice()

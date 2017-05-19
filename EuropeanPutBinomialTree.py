
from binomial import StockBinomialTree as bintree1
from binomial2 import bintree as bintree2
from binomial3 import bintree as bintree3

if __name__ == '__main__':
    euroPut = bintree1.EuropeanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print euroPut.getPrice()

    euroPut2 = bintree2.EuropeanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print euroPut2.getPrice()

    euroPut3 = bintree3.EuropeanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print euroPut3.getPrice()



from binomial import StockBinomialTree as bintree1
from binomial2 import bintree as bintree2
from binomial3 import bintree as bintree3

if __name__ == '__main__':
    amPut = bintree1.AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut.getPrice()

    amPut2 = bintree2.AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut2.getPrice()

    amPut3 = bintree3.AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut3.getPrice()
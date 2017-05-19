
from binomial import StockBinomialTree as bintree1
from binomial2 import bintree as bintree2
from binomial3 import bintree as bintree3

if __name__ == '__main__':
    amCall = bintree1.AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall.getPrice()

    amCall2 = bintree2.AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall2.getPrice()

    amCall3 = bintree3.AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall3.getPrice()
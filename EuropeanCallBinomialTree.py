
from binomial import StockBinomialTree as bintree1
from binomial2 import bintree as bintree2
from binomial3 import bintree as bintree3

if __name__ == '__main__':
    euroCall = bintree1.EuropeanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1, T=4, no_steps=4)
    print euroCall.getPrice()

    euroCall2 = bintree2.EuropeanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1, T=4, no_steps=4)
    print euroCall2.getPrice()

    euroCall3 = bintree3.EuropeanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1, T=4, no_steps=4)
    print euroCall3.getPrice()


from binomial.StockBinomialTree import EuropeanCallBinomialTree
from binomial2 import bintree

if __name__ == '__main__':
    euroCall = EuropeanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1, T=4, no_steps=4)
    print euroCall.getPrice()

    euroCall2 = bintree.EuropeanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1, T=4, no_steps=4)
    print euroCall2.getPrice()

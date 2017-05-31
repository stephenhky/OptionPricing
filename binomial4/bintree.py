

import numpy as np
from binomialtree import binomialtree as bt


class StockBinomialTree:
    '''
    Class that implements the binomial tree with stock price
    '''

    def __init__(self, S0=1.0, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.no_steps = no_steps

        self.price = 0
        self.initializeParameters()
        # self.initializeOptionPriceTree()

    def initializeParameters(self):
        self.dt = self.T / self.no_steps
        self.rdt = self.r * self.dt
        self.sigma2dt = self.sigma * self.sigma * self.dt
        self.u = np.exp(np.sqrt(self.sigma2dt))
        self.d = 1. / self.u
        self.p = (np.exp(self.rdt)-self.d) / (self.u-self.d)

    def get_stockprice(self, i, j):
        return bt.tree_stockprice(self.S0, self.u, self.d, i, j)

    def getPrice(self):
        return self.price

    def calculateOptionPriceTree(self):
        raise Exception('Not implemented!')


class EuropeanCallBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for European call option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, no_steps=no_steps)
        self.X = X
        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        self.price = bt.eurocall(self.S0, self.X, self.rdt, self.p, self.u, self.d, self.no_steps)


class EuropeanPutBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for European put option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, no_steps=no_steps)
        self.X = X
        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        self.price = bt.europut(self.S0, self.X, self.rdt, self.p, self.u, self.d, self.no_steps)


class AmericanCallBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for American call option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, no_steps=no_steps)
        self.X = X

        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        self.price = bt.amcall(self.S0, self.X, self.rdt, self.p, self.u, self.d, self.no_steps)


class AmericanPutBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for American put option
    '''

    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, no_steps=no_steps)
        self.X = X

        self.calculateOptionPriceTree()

    def calculateOptionPriceTree(self):
        self.price = bt.amput(self.S0, self.X, self.rdt, self.p, self.u, self.d, self.no_steps)

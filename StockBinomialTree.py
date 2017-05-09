'''
Created on Apr 11, 2013

@author: hok1
'''

import numpy as np

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
        
        self.initializeParameters()
        self.initializeStockTree()
        self.initializeOptionPriceTree()
        
    def initializeParameters(self):
        self.dt = self.T / self.no_steps
        self.rdt=self.r*self.dt
        self.sigma2dt=self.sigma*self.sigma*self.dt
        self.p=0.65
        p = self.p
        self.u = np.exp(self.rdt)+np.sqrt((1-p)/p*np.exp(0.5*self.sigma2dt))
        self.d = np.exp(-self.rdt)-np.sqrt(p/(1-p)*np.exp(0.5*self.sigma2dt))
        
    def initializeStockTree(self):
        stockTree = []
        for i in range(self.no_steps+1):
            stock = [self.S0*self.u**(i-j)*self.d**(j) for j in range(i+1)]
            stockTree.append(stock)
        self.stockTree = stockTree
        
    def initializeOptionPriceTree(self):
        optionPriceTree = []
        for i in range(self.no_steps+1):
            optionPrice = [0] * (i+1)
            optionPriceTree.append(optionPrice)
        self.optionPriceTree = optionPriceTree

    def getPrice(self):
        return self.optionPriceTree[0][0]

    def calculateOptionPriceTree(self):
        raise Exception('Not implemented!')
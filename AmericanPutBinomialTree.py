
from StockBinomialTree import StockBinomialTree
import numpy as np

class AmericanPutBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for American put option
    '''


    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        StockBinomialTree.__init__(self, S0=S0, r=r, sigma=sigma, T=T, no_steps=no_steps)
        self.T = T
        
        self.calculateOptionPriceTree()
        
    def calculateOptionPriceTree(self):
        for j in range(self.no_steps+1):
            self.optionPriceTree[self.no_steps][j] = max(self.X-self.stockTree[self.no_steps][j], 0)
        for i in range(self.no_steps-1, -1, -1):
            for j in range(i+1):
                imValue = self.X - self.stockTree[i][j]
                euroPutValue = np.exp(-self.rdt)*(self.p*self.optionPriceTree[i+1][j]+(1-self.p)*self.optionPriceTree[i+1][j+1])
                self.optionPriceTree[i][j] = max(imValue, euroPutValue)

if __name__ == '__main__':
    amPut = AmericanPutBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amPut.getPrice()
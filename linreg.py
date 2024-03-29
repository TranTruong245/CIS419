'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Vishnu Purushothaman Sreenivasan
'''
import numpy as np
from numpy import arange, linalg as LA
import matplotlib.pyplot as plt


class LinearRegression:

    def __init__(self, init_theta=None, alpha=0.01, n_iter=100):
        '''
        Constructor
        '''
        self.alpha = alpha
        self.n_iter = n_iter
        self.theta = init_theta
        self.JHist = None
    

    def gradientDescent(self, X, y, theta):
        '''
        Fits the model via gradient descent
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
            theta is a d-dimensional numpy vector
        Returns:
            the final theta found by gradient descent
        '''
        n,d = X.shape
        self.JHist = []    
        for i in arange(self.n_iter):
            self.JHist.append( (self.computeCost(X, y, theta), theta) )
            print ("Iteration: ", i+1, " Cost: ", self.JHist[i][0], " Theta: ", theta)
            # TODO:  add update equation here
            n,d = X.shape
            thetaDimensions,b = theta.shape     
            corrections = [0] * thetaDimensions

            for j in range(0,n):
                for thetaDimension in range(0,thetaDimensions):
                    corrections[thetaDimension] += (theta.getT()*X[j,:].getT() - y[j])*X[j,thetaDimension]
            for thetaDimension in range(0,thetaDimensions):
                theta[thetaDimension] = theta[thetaDimension] - corrections[thetaDimension]*(self.alpha/n)               
        return theta

    def computeCost(self, X, y, theta):
        '''
        Computes the objective function
        Arguments:
          X is a n-by-d numpy matrix
          y is an n-dimensional numpy vector
          theta is a d-dimensional numpy vector
        Returns:
          a scalar value of the cost  
              ** make certain you don't return a matrix with just one value! **
        '''
        # TODO: add objective (cost) equation here
        n,d = X.shape
        cost = (X*theta - y).getT()*(X*theta - y)/(2*n)
        return cost[0,0]

    def fit(self, X, y):
        '''
        Trains the model
        Arguments:
            X is a n-by-d numpy matrix
            y is an n-dimensional numpy vector
        '''
        n = len(y)
        n,d = X.shape
        if self.theta is None:
            self.theta = np.matrix(np.zeros((d,1)))
        self.theta = self.gradientDescent(X,y,self.theta)    
        


    def predict(self, X):
        '''
        Used the model to predict values for each instance in X
        Arguments:
            X is a n-by-d numpy matrix
        Returns:
            an n-dimensional numpy vector of the predictions
        '''
        return X*self.theta
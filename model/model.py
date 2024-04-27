import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import arviz as az
from scipy.stats import poisson

class bayesian_model:
    def __init__(self, parameter_path):
        self.parameters = pd.read_pickle(parameter_path)
        self.alpha = self.parameters['alpha']
        self.beta = self.parameters['beta']
        self.hw = self.parameters['hw']

    def predict(self, home_X, away_X, frame=1):
        if type(home_X) == list:
            home_X = np.array(home_X)
        if type(away_X) == list:
            away_X = np.array(away_X)
        if (home_X.shape != (9,)) & (away_X.shape != (9,)):
            raise Exception("wrong input shape. h : {} a : {}".format(home_X.shape, away_X.shape))
        
        h_lambda = np.exp((home_X * self.alpha[frame]).sum() + self.beta + self.hw)
        a_lambda = np.exp((away_X * self.alpha[frame]).sum() + self.beta)
        
        h_goal = home_X[2]
        a_goal = away_X[2]

        h_poisson = poisson((1-(frame/20))*h_lambda)
        a_poisson = poisson((1-(frame/20))*a_lambda)

        results = h_poisson.rvs(1000) - a_poisson.rvs(1000) + h_goal - a_goal
        win_p = ((results>0).sum()/1000, (results==0).sum()/1000, (results<0).sum()/1000)

        return win_p

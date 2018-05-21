import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


class GBRmodel:
    '''
    Optimized model for predicting wine score on an 80-100 point scale. X data
    should be a numpy matrix of pixel averages from landsat 8 satellite images.
    y data are Pinot Noir wine scores from Wine Enthusiast. Uses 9 gbr models
    on 9 spectral channels of landsat images, and an additional gbr model on the
    output of those 9 channel models.
    '''

    def __init__(self):
        '''define all 10 gbr models'''
        self.gbr0 = GradientBoostingRegressor()
        self.gbr1 = GradientBoostingRegressor()
        self.gbr2 = GradientBoostingRegressor()
        self.gbr3 = GradientBoostingRegressor()
        self.gbr4 = GradientBoostingRegressor()
        self.gbr6 = GradientBoostingRegressor()
        self.gbr7 = GradientBoostingRegressor()
        self.gbr9 = GradientBoostingRegressor()
        self.gbr10 = GradientBoostingRegressor()
        self.gbrfinal = GradientBoostingRegressor(alpha=0.5,n_estimators=50)


    def featurize(self,X):
        '''
        Takes numpy 2d matrix of avg pixel values, returns list of numpy 2d
        arrays. Convert raw mean of median pixel values to matrices of features
        to be used in training or predicting
        '''
        #Select only pixel values from the growing season
        X = X[:,36:216]

        #break data up into the spectral bands that will be used
        indexes = np.arange(0,180)
        band0 = X[:,indexes%12 == 0]
        band1 = X[:,indexes%12 == 1]
        band2 = X[:,indexes%12 == 2]
        band3 = X[:,indexes%12 == 3]
        band4 = X[:,indexes%12 == 4]
        band6 = X[:,indexes%12 == 6]
        band7 = X[:,indexes%12 == 7]
        band9 = X[:,indexes%12 == 9]
        band10 = X[:,indexes%12 == 10]

        return [band0,band1,band2,band3,band4,band6,band7,band9,band10]


    def fit(self,X,y):
        '''
        Trains a GradientBoostingRegressor on each spectral band,
        predicts a value for a vineyard, then trains a final GBR
        on the predicted values from each spectral band.
        '''
        bands = self.featurize(X)
        regressors = [self.gbr0,self.gbr1,self.gbr2,self.gbr3,self.gbr4,self.gbr6,
            self.gbr7,self.gbr9,self.gbr10]

        X_stacked = np.zeros((X.shape[0],len(regressors)))
        for i, _ in enumerate(bands):
            gbrmodel = regressors[i]
            gbrmodel.fit(bands[i],y)
            y_band = gbrmodel.predict(bands[i])
            X_stacked[:,i] = y_band

        self.gbrfinal.fit(X_stacked,y)
        return self


    def predict(self,X):
        '''
        Predicts scores from 9 channel models and the stacked final model.
        Outputs only the predicted values from the final model.
        '''
        bands = self.featurize(X)
        regressors = [self.gbr0,self.gbr1,self.gbr2,self.gbr3,self.gbr4,self.gbr6,
            self.gbr7,self.gbr9,self.gbr10]

        X_stacked = np.zeros((X.shape[0],len(regressors)))
        for i, _ in enumerate(bands):
            gbrmodel = regressors[i]
            y_band = gbrmodel.predict(bands[i])
            X_stacked[:,i] = y_band

        y = self.gbrfinal.predict(X_stacked)
        return y


if __name__ == '__main__':
    import pandas as pd
    from numpy import genfromtxt

    df = pd.read_csv('../data/pinot_noir_with_path_row.csv')
    y = df.points.values
    Xmean = genfromtxt('Xmean.csv', delimiter=',')

    gbr = GBRmodel()
    gbr.fit(Xmean,y)

    Xmean2017 = genfromtxt('Xmean2017.csv', delimiter=',')
    yy = gbr.predict(Xmean2017)

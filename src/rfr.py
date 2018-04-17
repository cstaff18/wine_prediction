import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.metrics import mean_squared_error



X = np.load('X.npy')
y = np.load('y.npy')

y_avg = np.mean(y)
rmse_base = np.sqrt(mean_squared_error(y,np.full(y.shape,y_avg)))
print('RMSE guessing the mean: ', rmse_base)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
rfr = rfr = RandomForestRegressor(n_estimators= 500)

rfr.fit(Xtrain,ytrain)
y_hat = rfr.predict(Xtest)
rmse_rf = np.sqrt(mean_squared_error(ytest,y_hat))
print('RMSE of Random Forest: ', rmse_rf)

feat = rfr.feature_importances_
band_import = feat.reshape(15,12)
band_import = band_import.T

nrow = 6; ncol = 2;
fig, axs = plt.subplots(nrows=nrow, ncols=ncol, figsize = (20,30))


colors = ['#000099','#0066ff','#33cc33','#cc3300','#800000','#ff6666','#ff9999','#ff9999','#99ffcc','#ff6666','#ffb3b3','#000000']

i = 0
for ax in axs.reshape(-1):
    ax.set_title('Band {}'.format(i+1), fontsize = 20)
    ax.set_ylim([0,0.06])
    ax.bar(range(15),band_import[i,:],color = colors[i])
    i += 1

plt.suptitle('Random Foresr Feature Importances',fontsize = 40)
plt.tight_layout(pad = 9)
plt.show()

sns.violinplot(y)
plt.title('Distribution of Scores')
plt.show()

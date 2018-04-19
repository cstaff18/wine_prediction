import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold, train_test_split



X = np.load('./data/X.npy')
y = np.load('./data/y.npy')

X2 = np.load('./data/X2.npy')
y2 = np.load('./data/y2.npy')

X = np.concatenate((X,X2),axis = 0)
y = np.concatenate((y,y2),axis = 0)

y_avg = np.mean(y)
rmse_base = np.sqrt(mean_squared_error(y,np.full(y.shape,y_avg)))
print('RMSE guessing the mean: ', rmse_base)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
rfr = RandomForestRegressor(n_estimators= 500)

# rfr.fit(Xtrain,ytrain)
# y_hat = rfr.predict(Xtest)
# rmse_rf = np.sqrt(mean_squared_error(ytest,y_hat))
# print('RMSE of Random Forest: ', rmse_rf)

kf = KFold(n_splits=5)

results = cross_val_score(rfr, Xtrain, ytrain, cv = kf)

print(results)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))


# feat = rfr.feature_importances_
# band_import = feat.reshape(15,12)
# band_import = band_import.T
#
# nrow = 6; ncol = 2;
# fig, axs = plt.subplots(nrows=nrow, ncols=ncol, figsize = (20,30))
#
#
# colors = ['#000099','#0066ff','#33cc33','#cc3300','#800000','#ff6666','#ff9999','#000000','#99ffcc','#ff6666','#ffb3b3','#000000']

# i = 0
# for ax in axs.reshape(-1):
#     ax.set_title('Band {}'.format(i+1), fontsize = 20)
#     ax.set_ylim([0,0.06])
#     ax.bar(range(15),band_import[i,:],color = colors[i])
#     i += 1
#
# plt.suptitle('Random Forest Feature Importances',fontsize = 40)
# plt.tight_layout(pad = 9)
# plt.savefig('rfr-feat-import.png')
# plt.show()
#
# sns.violinplot(y)
# plt.title('Distribution of Scores')
# plt.savefig('PN-score-dist.png')
# plt.show()

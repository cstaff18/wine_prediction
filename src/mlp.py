import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
import theano
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler
from keras.callbacks import TensorBoard
import tensorflow as tf

'''
exploring basic mlp architectures for predicting wine quality
'''


def define_nn_mlp_model(n_1 = 350,n_2 = 350,activ = 'elu'):
    ''' defines multi-layer-perceptron neural network '''

    model = Sequential() # sequence of layers
    num_neurons_in_layer = n_1
    num_inputs = 180
    model.add(Dense(units=num_neurons_in_layer,
                    input_dim=num_inputs,
                    kernel_initializer='normal',
                    activation=activ))


    model.add(Dense(units=n_2,
                    kernel_initializer='normal',
                    activation=activ))

    model.add(Dense(units=1,
                    kernel_initializer='normal',
                    ))
                    # keep softmax as last layer
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


if __name__ == '__main__':
    sess = tf.Session()


    rng_seed = 2 # set random number generator seed

    X = np.load('X2.npy')
    y = np.load('y2.npy')

    X2 = np.load('X2.npy')
    y2 = np.load('y2.npy')

    X = np.concatenate((X,X2),axis = 0)
    y = np.concatenate((y,y2),axis = 0)

    ss = StandardScaler()
    X = ss.fit_transform(X)
    # Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)

    np.random.seed(rng_seed)

    estimator = KerasRegressor(build_fn = define_nn_mlp_model, epochs = 1000, batch_size = 4)

    kf = KFold(n_splits=5)

    results = cross_val_score(estimator, X, y, cv = kf)

    print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

    file_writer = tf.summary.FileWriter('/logs', sess.graph)

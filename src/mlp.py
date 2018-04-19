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


def define_nn_mlp_model(n_1 = 350,n_2 = 350,activ = 'elu'):
    ''' defines multi-layer-perceptron neural network '''
    # available activation functions at:
    # https://keras.io/activations/
    # https://en.wikipedia.org/wiki/Activation_function
    # options: 'linear', 'sigmoid', 'tanh', 'relu', 'softplus', 'softsign'
    # there are other ways to initialize the weights besides 'uniform', too

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

# def print_output(model, y_train, y_test, rng_seed):
#     '''prints model accuracy results'''
#     y_train_pred = model.predict_classes(X_train, verbose=0)
#     y_test_pred = model.predict_classes(X_test, verbose=0)
#     print('\nRandom number generator seed: {}'.format(rng_seed))
#     print('\nFirst 30 labels:      {}'.format(y_train[:30]))
#     print('First 30 predictions: {}'.format(y_train_pred[:30]))
#     train_acc = np.sum(y_train == y_train_pred, axis=0) / X_train.shape[0]
#     print('\nTraining accuracy: %.2f%%' % (train_acc * 100))
#     test_acc = np.sum(y_test == y_test_pred, axis=0) / X_test.shape[0]
#     print('Test accuracy: %.2f%%' % (test_acc * 100))
#     if test_acc < 0.95:
#         print("\nMan, that's a poor test accuracy.")
#         print("Can't you get it up to 95%?")
#     else:
#         print("\nYou've made some improvements, I see...")


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

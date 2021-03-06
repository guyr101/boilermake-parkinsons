import numpy
import pickle as p
import datetime, time
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

data = p.load(open("train_model/picarray.pickle", "rb"))
X = numpy.array([row[0] for row in data])
y = numpy.array([row[1] for row in data])
pixel_size = len(X[0][0])

X = X.reshape(X.shape[0], 1, pixel_size, pixel_size).astype('float32')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

num_classes = 1

def baseline_model(convolutions=32, conv_size=10, pool_size=40, dropout=0.2, neurons=128):
	# create model
	model = Sequential()
	model.add(Conv2D(convolutions, (conv_size, conv_size), input_shape=(1, pixel_size, pixel_size), kernel_initializer='random_uniform', activation='relu'))
	model.add(MaxPooling2D(pool_size=(pool_size, pool_size)))
	model.add(Dropout(dropout))
	model.add(Flatten())
	model.add(Dense(neurons, activation='relu'))
	model.add(Dense(num_classes, activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

model = baseline_model()
# Fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, batch_size=20, verbose=2)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print(scores)
st = datetime.datetime.fromtimestamp(time.time()).strftime('%m%d%H%M%S')
model.save("Spiral_Model-"+str(round(scores[1]*100,2))+"-"+st+".h5")
print("Saved Model:","Spiral_Model-"+str(round(scores[1]*100,2))+"-"+st+".h5")
cm = confusion_matrix(y_test, [int(round(pred[0])) for pred in predictions])
print(cm)

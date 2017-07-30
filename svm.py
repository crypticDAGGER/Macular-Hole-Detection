import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import _pickle as pickle

clf = SVC()

X =pickle.load( open( "HOGX.p", "rb" ) )
y =pickle.load( open( "HOGy.p", "rb" ) )

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

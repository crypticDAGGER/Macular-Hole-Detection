import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import _pickle as pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit

Cval=[1,2,3,30, 40, 50, 60, 70 ,80, 90]

X =pickle.load( open( "HOGX.p", "rb" ) )
y =pickle.load( open( "HOGy.p", "rb" ) )

X=np.reshape(X,(163,1764))


print(y.shape, X.shape)
'''X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

print("Fitiing model...")
clf.fit(X_train, y_train)

print("Making predictions...")
y_pred=clf.predict(X_test)'''

for c in Cval:
    clf = SVC(kernel='linear',C=c)
    
    cv = ShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
    scores = cross_val_score(clf, X, y, cv=cv)
    print(scores)


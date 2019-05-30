import pandas as pd
import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import warnings
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
warnings.filterwarnings("ignore", category=FutureWarning)
# data = pd.read_csv("features.csv")
# data.head()

# print(data)
names = ['name of image','area','perimeter','aspect_ratio','equi_diameter','extent','convex_area','solidity','majoraxis_length','minoraxis_length','eccentricity','species']



dataframe = pd.read_csv("features.csv", names=names, header = 0)

#Convert string to Numeric
for name in names:  # Iterate over chosen columns
	dataframe[name] = pd.to_numeric(dataframe[name])

array = dataframe.values
# X = array[:,1:11]
# Y = array[:,11]
X = dataframe.iloc[:,1:11]  #independent columns
Y = dataframe.iloc[:,11]    #target column i.e price range
# print(X)
# print(array[0,0])
#Feature extraction
# model = LogisticRegression()
model = ExtraTreesClassifier()
# rfe = RFE(model, 6)
# fit = rfe.fit(X, Y)
model.fit(X,Y)
print(model.feature_importances_)
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()
# print("Num Features: %s" % (fit.n_features_))
# print("Selected Features: %s" % (fit.support_))
# print("Feature Ranking: %s" % (fit.ranking_))

# Num Features: 6
# Selected Features: [False False  True  True  True False  True False  True  True]
# Feature Ranking: [4 3 1 1 1 5 1 2 1 1]
# aspect_ratio
# equi_diameter
# extent
# solidity
# minoraxis_length
# eccentricity
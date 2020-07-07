from numpy import loadtxt
from xgboost import XGBClassifier
from matplotlib import pyplot
# load data
mydata = loadtxt('yourfile.csv', delimiter=",") # this could be txt, dm
# split data into X and y
# here i have 12 cols for one result
X = mydata[:,0:12] #affecting columns
y = mydata[:,12] #result column

# fit model no training data
model = XGBClassifier()
model.fit(X, y)
# feature importance
print(model.feature_importances_)
# plot
pyplot.bar(range(len(model.feature_importances_)), model.feature_importances_)
pyplot.show()

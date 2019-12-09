from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

X = pickle.load(open('Pickle_files/midPerChX.pickle','rb'))
y = pickle.load(open('Pickle_files/midPerChY.pickle','rb'))
X_train,X_test,y_train,y_test = train_test_split(X,y)

regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
print(y_pred,y_test)

pickle_out = open("Pickle_files/modelTTBDMid.pickle","wb")
pickle.dump(regressor,pickle_out)
pickle_out.close()
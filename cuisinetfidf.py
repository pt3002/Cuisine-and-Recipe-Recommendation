import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import config
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

test_df = pd.read_csv(config.RECIPES_PATH)
cuisine_df = pd.read_csv(config.RECIPES_PATH)

vect = TfidfVectorizer(binary=True).fit(cuisine_df['Ingredients'].values)
X_train_vectorized = vect.transform(cuisine_df['Ingredients'].values)
X_train_vectorized = X_train_vectorized.astype('float')

Result_transformed = vect.transform(test_df['Ingredients'].values)
Result_transformed = Result_transformed.astype('float')

encoder = LabelEncoder()
y_transformed = encoder.fit_transform(cuisine_df.Cuisine)
X_train, X_test, y_train, y_test = train_test_split(X_train_vectorized, y_transformed , random_state = 0)

clf1 = LogisticRegression(solver='lbfgs', max_iter=1000)
clf1.fit(X_train , y_train)
print(clf1.score(X_test, y_test))

vclf=VotingClassifier(estimators=[('clf1',LogisticRegression(solver='lbfgs', max_iter=1000)),('clf2',SVC(C=100,gamma=1,kernel='rbf',probability=True))],voting='soft',weights=[1,2])
vclf.fit(X_train , y_train)
print(vclf.score(X_test, y_test))

pickle.dump(vclf, open(config.CUISINE_MODEL_PATH, 'wb'))
pickled_model = pickle.load(open(config.CUISINE_MODEL_PATH, 'rb'))
y_predicted = vclf.predict(Result_transformed)
y_predicted_final = encoder.inverse_transform(y_predicted)
predictions = pd.DataFrame({'cuisine' : y_predicted_final})
predictions = predictions[['cuisine']]
predictions.to_csv('submit.csv', index = False)
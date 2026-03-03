import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("student_scores.csv")

X = data[['hours','attendance','sleep']]
y = data['marks']

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully!")
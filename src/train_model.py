import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

#data = pd.read_csv("../data/sample_solar_data.csv")
data = pd.read_csv("data/sample_solar_data.csv")

X = data[["sunlight_hours","temperature"]]
y = data["solar_output"]

model = LinearRegression()
model.fit(X,y)

joblib.dump(model,"solar_model.pkl")

print("Model trained and saved.")

import joblib

model = joblib.load("solar_model.pkl")

sunlight = float(input("Enter sunlight hours: "))
temp = float(input("Enter temperature: "))

prediction = model.predict([[sunlight,temp]])

print("Predicted Solar Output:", round(prediction[0],2),"kWh")

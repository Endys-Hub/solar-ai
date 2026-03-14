import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/sample_solar_data.csv")

plt.scatter(data["sunlight_hours"], data["solar_output"])

plt.title("Solar Output vs Sunlight Hours")
plt.xlabel("Sunlight Hours")
plt.ylabel("Solar Output (kWh)")

plt.savefig("../images/solar_output_vs_sunlight.png")
plt.show()

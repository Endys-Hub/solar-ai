import matplotlib.pyplot as plt
import numpy as np

# Chart 1: Solar Output vs Sunlight Hours
sunlight_hours = np.array([3,4,5,6,7,8,9])
solar_output = np.array([0.9,1.2,1.6,2.1,2.6,3.0,3.4])

plt.scatter(sunlight_hours, solar_output, color="orange")
plt.plot(sunlight_hours, solar_output, color="blue")

plt.title("Solar Energy Output vs Sunlight Hours")
plt.xlabel("Sunlight Hours")
plt.ylabel("Solar Output (kWh)")
plt.grid(True)

plt.savefig("../images/solar_output_vs_sunlight.png")
plt.clf()

# Chart 2: Daily Solar Production
hours = np.arange(6,19)
production = np.maximum(0, np.sin((hours-6)/12*np.pi))*3

plt.plot(hours, production, color="green")

plt.title("Typical Daily Solar Production")
plt.xlabel("Hour of Day")
plt.ylabel("Solar Power (kW)")
plt.grid(True)

plt.savefig("../images/daily_solar_production.png")
plt.clf()

# Chart 3: AI Workflow Diagram
fig, ax = plt.subplots(figsize=(10,3))
ax.axis('off')

boxes = [
("Weather Data",0.1),
("AI Model",0.4),
("Solar Prediction",0.7),
("Energy Advice",0.9)
]

for text,x in boxes:
    ax.text(x,0.5,text,
            ha='center',
            va='center',
            bbox=dict(boxstyle="round,pad=0.4",fc="lightblue"))

for i in range(len(boxes)-1):
    ax.annotate("",
                xy=(boxes[i+1][1]-0.07,0.5),
                xytext=(boxes[i][1]+0.07,0.5),
                arrowprops=dict(arrowstyle="->"))

plt.savefig("../images/solar_ai_workflow.png")

print("Images generated successfully!")
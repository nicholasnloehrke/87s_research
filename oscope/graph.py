import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("RigolDS3.csv")

x = data["Time(s)"]
y = data["CH1V"]

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker="o")
plt.title("Time vs. Voltage")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.show()

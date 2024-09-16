import math
import matplotlib.pyplot as plt
import numpy as np

# Parameters
NUM_RESISTORS = 8  # Number of resistors to use
RESISTANCE_MIN = 1  # Minimum resistance in Ohms
RESISTANCE_MAX = 10000  # Maximum resistance in Ohms
MAX_VOLTAGE = 12  # Maximum voltage in Volts

# Generate resistor values within the specified range
resistor_values = np.logspace(np.log10(RESISTANCE_MIN), np.log10(RESISTANCE_MAX), num=NUM_RESISTORS, base=10)

def parallel(resistors: list):
    summ = sum([1 / r for r in resistors])
    return 1 / summ if summ > 0 else math.inf

def is_significantly_different(new_value, last_value, threshold):
    return abs(new_value - last_value) > threshold

# Define the range of resistor values
RESISTORS = resistor_values.tolist()
COMBINATIONS = [i for i in range(2**len(RESISTORS))]

# Create a dictionary to store combination to resistance mapping
combo_to_resistance = {}
all_resistors_used = set()

for combination in COMBINATIONS:
    included_resistors = [RESISTORS[i] for i in range(len(RESISTORS)) if combination & (1 << i)]
    resistance = parallel(included_resistors)
    if resistance != math.inf and 1 <= resistance <= RESISTANCE_MAX:
        combo_to_resistance[combination] = (resistance, included_resistors)
        all_resistors_used.update(included_resistors)

# Sort the dictionary by resistance value
sorted_combos = sorted(combo_to_resistance.items(), key=lambda item: item[1][0])

# Print the sorted combinations, resistances, and resistors used
for combo, (resistance, resistors) in sorted_combos:
    resistor_str = ', '.join(f'{r:.2f}' for r in resistors)
    print(f'{combo:0{len(RESISTORS)}b} : Resistance = {resistance:.2f} Ohms, Resistors used = [{resistor_str}]')

print(f'total combos: {len(sorted_combos)}')

# Print all resistors used across all combinations and their max power dissipation
print(f'\nAll resistors used in combinations and their max power dissipation:')
for resistor in sorted(all_resistors_used):
    max_power_dissipation = (MAX_VOLTAGE**2) / resistor  # P = V^2 / R
    print(f'{resistor:.2f} Ohms, Max Power Dissipation = {max_power_dissipation:.2f} W')
    
print()
print(sorted(all_resistors_used))

# Prepare data for plotting
resistances = [resistance for _, (resistance, _) in sorted_combos]

plt.figure(figsize=(10, 6))
plt.plot(resistances, marker='o', linestyle='-', color='b')
plt.title('Parallel Resistances for Different Combinations')
plt.xlabel('Combination Index')
plt.ylabel('Resistance (Ohms)')
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.grid(True, which="both", ls="--")
plt.show()

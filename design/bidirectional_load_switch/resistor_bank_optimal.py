import math
import matplotlib.pyplot as plt
import numpy as np

# parameters
NUM_RESISTORS = 8        # number of resistors to use
RESISTANCE_MIN = 1       # minimum resistance in Ω
RESISTANCE_MAX = 10000   # maximum resistance in Ω
SUPPLY_VOLTAGE = 12      # maximum voltage in Volts
SUPPLY_RESISTANCE = 10.2 # ESR of supply

# generate resistor values within the specified range
resistor_values = np.logspace(np.log10(RESISTANCE_MIN), np.log10(RESISTANCE_MAX), num=NUM_RESISTORS, base=10)

def parallel(resistors: list):
    summ = sum([1 / r for r in resistors])
    return 1 / summ if summ > 0 else math.inf

# define the range of resistor values
RESISTORS = resistor_values.tolist()
COMBINATIONS = [i for i in range(2**len(RESISTORS))]

# create a dictionary to store combination to resistance mapping
combo_to_resistance = {}
all_resistors_used = set()

for combination in COMBINATIONS:
    included_resistors = [RESISTORS[i] for i in range(len(RESISTORS)) if combination & (1 << i)]
    resistance = parallel(included_resistors)
    if resistance != math.inf and 1 <= resistance <= RESISTANCE_MAX:
        combo_to_resistance[combination] = (resistance, included_resistors)
        all_resistors_used.update(included_resistors)

# sort the dictionary by resistance value
sorted_combos = sorted(combo_to_resistance.items(), key=lambda item: item[1][0])

# print the sorted combinations, resistances, and resistors used
for combo, (resistance, resistors) in sorted_combos:
    resistor_str = ', '.join(f'{r:.2f}' for r in resistors)
    print(f'{combo:0{len(RESISTORS)}b} : Resistance = {resistance:.2f}Ω, Resistors used = [{resistor_str}]')

# print all resistors used across all combinations and their max power dissipation
print(f'\nMax electrical load per resistor. Vs: {SUPPLY_VOLTAGE:.2f}V, Rs: {SUPPLY_RESISTANCE:.2f}Ω:')
for resistor in sorted(all_resistors_used):
    current = SUPPLY_VOLTAGE / (resistor + SUPPLY_RESISTANCE)
    voltage = (SUPPLY_VOLTAGE * resistor) / (resistor + SUPPLY_RESISTANCE)
    power = current * voltage
    print(f'{resistor:.2f}Ω : {power:.2f}W {current:.2f}A {voltage:.2f}V')
    
print("\nResistor list:")
print(sorted(all_resistors_used))

# prepare data for plotting
resistances = [resistance for _, (resistance, _) in sorted_combos]

plt.figure(figsize=(10, 6))
plt.plot(resistances, marker='o', linestyle='-', color='b')
plt.title('Parallel Resistances for Different Combinations')
plt.xlabel('Combination Index')
plt.ylabel('Resistance (Ω)')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()

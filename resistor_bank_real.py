import math
import matplotlib.pyplot as plt

RESISTORS = [1.0, 3.72759372031494, 13.894954943731374, 51.7947467923121, 193.06977288832496, 719.6856730011514, 2682.6957952797247, 10000.0]
THRESHOLD = 10

COMBINATIONS = [i for i in range(2**len(RESISTORS))]

def parallel(resistors: list):
    summ = sum([1 / r for r in resistors])
    return 1 / summ if summ > 0 else math.inf

def is_significantly_different(new_value, last_value, threshold):
    return abs(new_value - last_value) > threshold

# Create a dictionary to store combination to resistance mapping
combo_to_resistance = {}

for combination in COMBINATIONS:
    included_resistors = [RESISTORS[i] for i in range(len(RESISTORS)) if combination & (1 << i)]
    resistance = parallel(included_resistors)
    combo_to_resistance[combination] = resistance

# Sort the dictionary by resistance value
sorted_combos = sorted(combo_to_resistance.items(), key=lambda item: item[1])

# Print the sorted combinations and resistances
for combo, resistance in sorted_combos:
    print(f'{combo:0{len(RESISTORS)}b} : {resistance:.2f}')

print(f'total combos: {len(sorted_combos)}')

# Prepare data for plotting
resistances = [resistance for _, resistance in sorted_combos]

plt.figure(figsize=(10, 6))
plt.plot(resistances, marker='o', linestyle='-', color='b')
plt.title('Parallel Resistances for Different Combinations')
plt.xlabel('Combination Index')
plt.ylabel('Resistance (Ohms)')
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.grid(True, which="both", ls="--")
plt.show()

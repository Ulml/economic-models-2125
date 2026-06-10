import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2025, 2126, 5)

def simulate_purchasing_power(initial=100, scenario='realiste'):
    power = np.zeros(len(years))
    power[0] = initial
    for i in range(1, len(years)):
        y = years[i]
        if scenario == 'optimiste':
            rate = 0.025 if y < 2050 else 0.018
        elif scenario == 'realiste':
            rate = 0.015 if y < 2050 else 0.008
        else:  # pessimiste
            rate = 0.005 if y < 2045 else -0.01
        power[i] = power[i-1] * (1 + rate)
    return power

plt.figure(figsize=(12, 7))
scenarios = ['optimiste', 'realiste', 'pessimiste']
colors = ['green', 'blue', 'red']

for i, scen in enumerate(scenarios):
    power = simulate_purchasing_power(scenario=scen)
    plt.plot(years, power, label=scen.capitalize(), color=colors[i], linewidth=2.5)

plt.title('Pouvoir d\'achat d\'un retraité de 75 ans jusqu\'en 2125 (index 100 en 2025)')
plt.xlabel('Année')
plt.ylabel('Pouvoir d\'achat relatif')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('retiree_purchasing_power.png')
plt.show()
print('Graphique sauvegardé : retiree_purchasing_power.png')
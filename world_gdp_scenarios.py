import numpy as np
import matplotlib.pyplot as plt

# Années
years = np.arange(1960, 2130, 5)

def simulate_gdp(initial_gdp=20e12, scenario='realiste'):
    gdp = np.zeros(len(years))
    gdp[0] = initial_gdp
    for i in range(1, len(years)):
        y = years[i]
        if scenario == 'optimiste':
            if y < 2040:
                rate = 0.035
            elif y < 2060:
                rate = 0.045
            else:
                rate = 0.025
        elif scenario == 'realiste':
            if y < 2040:
                rate = 0.032
            elif y < 2060:
                rate = 0.022
            elif y < 2090:
                rate = 0.016
            else:
                rate = 0.012
        else:  # pessimiste
            if y < 2040:
                rate = 0.032
            elif y < 2060:
                rate = 0.012
            elif y < 2090:
                rate = -0.005
            else:
                rate = 0.003
        gdp[i] = gdp[i-1] * (1 + rate)
    return gdp

# Générer les trois scénarios
plt.figure(figsize=(12, 7))
scenarios = ['optimiste', 'realiste', 'pessimiste']
colors = ['green', 'blue', 'red']

for i, scen in enumerate(scenarios):
    gdp = simulate_gdp(scenario=scen)
    plt.plot(years, gdp / 1e12, label=scen.capitalize(), color=colors[i], linewidth=2.5)

plt.title('Projections PIB Mondial jusqu\'en 2125 (trillions USD constants)')
plt.xlabel('Année')
plt.ylabel('PIB Mondial (trillions USD)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('world_gdp_scenarios.png')
plt.show()
print('Graphique sauvegardé : world_gdp_scenarios.png')
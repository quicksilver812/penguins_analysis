# Creating a violin plot for body mass by species and sex

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('penguins.csv')

fig, ax = plt.subplots(figsize=(10, 6))
sns.violinplot(x='species', y='body_mass_g', hue='sex', data=df, split=True, palette='Set2')
ax.set_title('Body Mass Distribution by Species and Sex')
ax.set_xlabel('Species')
ax.set_ylabel('Body Mass (g)')
plt.show()
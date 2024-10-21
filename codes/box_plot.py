# Creating a box plot for body mass by species and island

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('penguins.csv')

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='species', y='body_mass_g', hue='island', data=df, palette='Set2')
ax.set_title('Body Mass Distribution by Species and Island')
ax.set_xlabel('Species')
ax.set_ylabel('Body Mass (g)')
plt.show()
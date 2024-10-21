# Creating a heatmap showing correlation between physical characteristics

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('penguins.csv')

corr_matrix = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Physical Characteristics')
plt.show()
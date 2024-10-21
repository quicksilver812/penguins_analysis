# Creating a bar plot with mean flipper length for each species

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('penguins.csv')

mean_flipper_length = df.groupby('species')['flipper_length_mm'].mean()

plt.figure(figsize=(8, 6))
mean_flipper_length.plot(kind='bar')
plt.title('Average Flipper Length by Species')
plt.xlabel('Species')
plt.ylabel('Flipper Length (mm)')
plt.show()
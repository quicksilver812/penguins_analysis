# Create a scatter plot for bill length vs. bill depth, colored by species

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('penguins.csv')

plt.figure(figsize=(8, 6))
for species, group in df.groupby('species'):
    plt.scatter(group['bill_length_mm'], group['bill_depth_mm'], label=species, alpha=0.5)
plt.title('Bill Length vs. Bill Depth by Species')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend()
plt.show()
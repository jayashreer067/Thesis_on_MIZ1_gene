import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.patches as patches

# Load the Excel file
file_path = 'synteny.xlsx'  # Ensure the file path is correct
df = pd.read_excel(file_path)

# Strip any leading or trailing spaces from the entire DataFrame
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Set the correct column as the index
df.set_index('Species_', inplace=True)

# Replace 'yes' with 1 for presence and NaN for absence
df_colors = df.replace('yes', 1).fillna(np.nan)

# Define a custom colormap where NaN is grey and presence is a chosen color
colors = ['#D3D3D3', '#4682B4']  # Light grey for NaN and Steel Blue for presence
cmap = mcolors.ListedColormap(colors)

# Plot the heatmap with the custom colormap
plt.figure(figsize=(12, 8))
ax = sns.heatmap(df_colors, annot=False, cmap=cmap, linewidths=.5, cbar=False, linecolor='white')

# Set the title and labels with highlighted font properties
plt.xlabel('Genes', fontsize=14, fontweight='bold', color='darkred')
plt.ylabel('Species', fontsize=14, fontweight='bold', color='darkred')

# Format the y-axis labels to italicize species names and handle underscores
species_formatted = [r"$\it{" + species.replace("_", "\ ") + "}$" for species in df_colors.index]
ax.set_yticklabels(species_formatted, rotation=0, fontsize=10)

# Draw a single outer border around the heatmap
ax.add_patch(patches.Rectangle((0, 0), df_colors.shape[1], df_colors.shape[0],
                               fill=False, edgecolor='black', lw=4))

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()

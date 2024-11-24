import matplotlib.pyplot as plt

# Define the tissue types and corresponding colors used in the bubble plot
tissue_types = {
    'root': '#1f77b4',
    'stem': '#ff7f0e',
    'flower': '#2ca02c',
    'leaf': '#d62728',
    'fruit': '#9467bd',
    'female reproductive part': '#8c564b',
    'male reproductive part': '#e377c2',
    'endosperm': '#7f7f7f',
    'seedling': '#bcbd22',
    'seeds': '#17becf',
    'archegonia': '#aec7e8',
    'sporophyte': '#ffbb78'
}

# Create a blank figure for the legend
plt.figure(figsize=(5, 7))

# Add legend items for each tissue type
for tissue, color in tissue_types.items():
    plt.scatter([], [], c=[color], label=tissue, edgecolor='black', s=200)

# Plot the legend
plt.legend(title="Tissue Type (Bubble Color)", loc='center', bbox_to_anchor=(0.5, 0.5))
plt.axis('off')

# Show the plot (legend only)
plt.tight_layout()
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'paralogs.xlsx'
df = pd.read_excel(file_path)

# Create a new column that combines species and whether there was expression in root during stress
df['Species with Stress'] = df['species']

# Map the expressions to numeric values for the heatmap
expression_map = {
    'root': 1,
    'stem': 2,
    'flower': 3,
    'leaf': 4,
    'fruit': 5,
    'female reproductive part': 6,
    'male reproductive part': 7,
    'endosperm': 8,
    'seedling': 9,
    'seeds': 10,
    'archegonia': 11,
    'sporophyte': 12,
    'shoot system': 13,
    'reproductive part': 14,
    None: 0  # Handle missing data
}

# Reverse map for annotations
reverse_expression_map = {v: k for k, v in expression_map.items()}

# Replace the expressions with their mapped numeric values
df['Highest expression'] = df['Highest expression'].map(expression_map).astype(float)
df['2nd highest expression'] = df['2nd highest expression'].map(expression_map).astype(float)
df['3rd highest expression'] = df['3rd highest expression'].map(expression_map).astype(float)
df['least expression'] = df['least expression'].map(expression_map).astype(float)

# Create a DataFrame for the heatmap
heatmap_data = df.set_index('Species with Stress')[['Highest expression', '2nd highest expression', '3rd highest expression', 'least expression']]

# Set up the figure
plt.figure(figsize=(14, 10))

# Create a heatmap
ax = sns.heatmap(heatmap_data, annot=False, cmap="coolwarm", linewidths=.5, fmt=".1f", cbar=False)

# Add annotations with text instead of numbers
for i in range(heatmap_data.shape[0]):
    for j in range(heatmap_data.shape[1]):
        value = heatmap_data.iloc[i, j]
        if not pd.isna(value):
            # Annotate the heatmap with the actual tissue type
            ax.text(j + 0.5, i + 0.5, reverse_expression_map[value], color='black', ha='center', va='center')
            # Highlight cells with root expression during stress
            if df['In root during stress'].iloc[i] == 'yes' and reverse_expression_map[value] == 'root':
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=False, edgecolor='red', lw=3))

# Draw an outer border around the heatmap
ax.add_patch(plt.Rectangle((0, 0), heatmap_data.shape[1], heatmap_data.shape[0],
                           fill=False, edgecolor='black', lw=4, zorder=2))

# Rotate x-axis labels for better readability
plt.xticks(rotation=360, ha='center')

    # Set the title and labels with highlighted font properties
    #plt.title('Gene Expression by Species and Stress Response in First Paralog', fontsize=16, fontweight='bold', color='navy')
    #plt.xlabel('Expression Rank', fontsize=14, fontweight='bold', color='navy')
    #plt.ylabel('Species with Gene Expression', fontsize=14, fontweight='bold', color='navy')

# Add a custom legend for the expression types
legend_labels = [f"{num}: {name}" for num, name in reverse_expression_map.items() if num != 0]
plt.figtext(1.02, 0.5, '\n'.join(legend_labels), wrap=True, horizontalalignment='left', fontsize=10)

# Add a note about the stress response
plt.figtext(0.02, 0.01, "Note: Cells with a red border indicate root expression\nunder abiotic stress conditions.", fontsize=10, color='red')

# Show the plot
plt.tight_layout()
plt.show()

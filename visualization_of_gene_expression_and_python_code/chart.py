import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = '.xlsx'
df = pd.read_excel(file_path)

# Create a new column that combines species and whether there was expression in root during stress
df['Species with Stress'] = df['species']

# Map the expressions to numeric values and assign specific colors for each tissue type
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
    None: 0  # Handle missing data
}

# Define the colors for each tissue type
tissue_colors = {
    1: '#1f77b4',   # root
    2: '#ff7f0e',   # stem
    3: '#2ca02c',   # flower
    4: '#d62728',   # leaf
    5: '#9467bd',   # fruit
    6: '#8c564b',   # female reproductive part
    7: '#e377c2',   # male reproductive part
    8: '#7f7f7f',   # endosperm
    9: '#bcbd22',   # seedling
    10: '#17becf',  # seeds
    11: '#aec7e8',  # archegonia
    12: '#ffbb78'   # sporophyte
}

# Reverse map for annotations
reverse_expression_map = {v: k for k, v in expression_map.items()}

# Replace the expressions with their mapped numeric values
df['Highest expression'] = df['Highest expression'].map(expression_map).astype(float)
df['2nd highest expression'] = df['2nd highest expression'].map(expression_map).astype(float)
df['3rd highest expression'] = df['3rd highest expression'].map(expression_map).astype(float)
df['least expression'] = df['least expression'].map(expression_map).astype(float)

# Melt the DataFrame for easier plotting
df_melted = df.melt(id_vars=['Species with Stress', 'In root during stress'],
                    value_vars=['Highest expression', '2nd highest expression', '3rd highest expression', 'least expression'],
                    var_name='Expression Rank',
                    value_name='Expression')

# Map the Expression Rank to readable labels
expression_rank_map = {
    'Highest expression': '1st Highest',
    '2nd highest expression': '2nd Highest',
    '3rd highest expression': '3rd Highest',
    'least expression': 'Least'
}
df_melted['Expression Rank'] = df_melted['Expression Rank'].map(expression_rank_map)

# Set up the figure
plt.figure(figsize=(16, 10))

# Plot the bubble chart with uniform bubble size
bubble_plot = sns.scatterplot(
    x='Species with Stress',
    y='Expression Rank',
    hue='Expression',
    data=df_melted,
    palette=tissue_colors,
    s=300,  # Set a uniform size for all bubbles
    edgecolor='black',
    legend=False
)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90, ha='center')

# Set the title and labels
plt.title('Gene Expression by Species and Stress Response')
plt.xlabel('Species with Gene Expression')
plt.ylabel('Expression Rank')

# Add a custom legend for the expression types on the left side
legend_labels = [f"{num}: {name}" for num, name in reverse_expression_map.items() if num != 0]
plt.figtext(-0.25, 0.5, '\n'.join(legend_labels), wrap=True, horizontalalignment='left', fontsize=10)

# Highlight bubbles for root expression during stress
for i in range(df_melted.shape[0]):
    value = df_melted['Expression'].iloc[i]
    if not pd.isna(value):
        tissue_type = reverse_expression_map.get(value, None)
        if df_melted['In root during stress'].iloc[i] == 'yes' and tissue_type == 'root':
            bubble_plot.scatter(
                i % len(df['Species with Stress'].unique()),
                i // len(df['Species with Stress'].unique()),
                s=500, facecolors='none', edgecolors='red', linewidth=2
            )

# Add a note about the stress response
plt.figtext(0.02, 0.01, "Note: Bubbles with a red border indicate root expression\nunder abiotic stress conditions.", fontsize=10, color='red')

# Show the plot
plt.tight_layout()
plt.show()

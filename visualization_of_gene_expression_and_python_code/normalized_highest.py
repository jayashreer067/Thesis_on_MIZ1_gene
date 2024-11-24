import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'paralog3.xlsx'
df = pd.read_excel(file_path)

# Map the expressions to human-readable labels (if needed)
expression_map = {
    'root': 'Root',
    'stem': 'Stem',
    'flower': 'Flower',
    'leaf': 'Leaf',
    'fruit': 'Fruit',
    'female reproductive part': 'Female Reproductive Part',
    'male reproductive part': 'Male Reproductive Part',
    'endosperm': 'Endosperm',
    'seedling': 'Seedling',
    'seed': 'Seeds',
    'archegonia': 'Archegonia',
    'sporophyte': 'Sporophyte',
    'sporeling at 24hr': 'Sporeling At 24hr',
    'shoot system': 'Shoot System',
    None: 'No Data'  # Handle missing data
}

# Apply the mapping to the DataFrame
df['Highest expression'] = df['Highest expression'].map(expression_map)
df['2nd highest expression'] = df['2nd highest expression'].map(expression_map)

# Combine the highest and second-highest expressions across all species
combined_expressions = pd.concat([df['Highest expression'], df['2nd highest expression']])

# Count the occurrences of each tissue type
expression_counts = combined_expressions.value_counts()

# Normalize by the total number of counts
normalized_expression = expression_counts / expression_counts.sum()

# Convert the series to a DataFrame for plotting
normalized_df = normalized_expression.reset_index()
normalized_df.columns = ['Tissue Type', 'Normalized Expression']

# Plotting the results
plt.figure(figsize=(10, 6))
sns.barplot(x='Tissue Type', y='Normalized Expression', data=normalized_df, palette='coolwarm', edgecolor='black')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Set the title and labels
#plt.title('Normalized Tissue Expression Across All Species for a Single Paralog', fontsize=16, fontweight='bold')
plt.xlabel('Plant Tissues and Organs', fontsize=14, fontweight='bold', ha='left')
plt.ylabel('Normalized Gene Expression in Third Paralog ', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

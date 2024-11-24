import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'paralog2.xlsx'
df = pd.read_excel(file_path)

# Map the expressions to human-readable labels
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
    None: 'No Data'  # Handle missing data
}

# Apply the mapping to the DataFrame
df['Highest expression'] = df['Highest expression'].map(expression_map)
df['2nd highest expression'] = df['2nd highest expression'].map(expression_map)

# Combine the 'Highest expression' and '2nd highest expression' into a single series
combined_expressions = pd.concat([df['Highest expression'], df['2nd highest expression']])

# Count the occurrences of each tissue type
expression_counts = combined_expressions.value_counts()

# Plot the results
plt.figure(figsize=(12, 8))
sns.barplot(x=expression_counts.index, y=expression_counts.values, palette='coolwarm', edgecolor='black')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Set the title and labels
plt.title('Frequency of Tissues in Highest and Second Highest Expression Across the second paralog', fontsize=16, fontweight='bold', color='navy')
plt.xlabel('Tissue Type', fontsize=14, fontweight='bold', color='navy')
plt.ylabel('Frequency of Expression', fontsize=14, fontweight='bold', color='navy')

# Add annotations to the bars
for i in range(len(expression_counts)):
    plt.text(i, expression_counts.values[i] + 0.1, str(expression_counts.values[i]), ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()

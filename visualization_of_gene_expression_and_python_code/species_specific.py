import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to your Excel file
file_path = 'species_expression.xlsx'

# Read the data from the Excel file
df = pd.read_excel(file_path)

# Initialize a list to store the normalized data
normalized_data = []

# Loop through each species
for species in df['Species'].unique():
    species_data = df[df['Species'] == species]

    # Drop NaN values (treat them as no expression)
    species_data_high = species_data[['Highest expression', '2nd highest expression']].dropna().melt()
    species_data_low = species_data[['3rd highest expression', 'least expression']].dropna().melt()

    # Count occurrences of each region in 'Highest' and '2nd highest' combined
    max_expression_counts = species_data_high['value'].value_counts()

    # Count occurrences of each region in '3rd highest' and 'Least' combined
    min_expression_counts = species_data_low['value'].value_counts()

    # Normalize by the total number of non-NaN entries for that species
    max_expression_counts_normalized = max_expression_counts / len(species_data_high)
    min_expression_counts_normalized = min_expression_counts / len(species_data_low)

    # Handle missing data by filling with 0
    all_regions = set(max_expression_counts_normalized.index).union(set(min_expression_counts_normalized.index))
    for region in all_regions:
        if region not in max_expression_counts_normalized:
            max_expression_counts_normalized[region] = 0
        if region not in min_expression_counts_normalized:
            min_expression_counts_normalized[region] = 0

    # Find the regions with maximum and minimum normalized expression
    max_expression_region = max_expression_counts_normalized.idxmax()
    min_expression_region = min_expression_counts_normalized.idxmax()

    # Append the result as a dictionary to the list
    normalized_data.append({
        'Species': species,
        'Max Expression Region': max_expression_region,
        'Min Expression Region': min_expression_region,
        'Max Expression Value': 2.5,  # Height of the max expression bar
        'Min Expression Value': 1  # Height of the min expression bar
    })

# Convert the list of dictionaries to a DataFrame
normalized_df = pd.DataFrame(normalized_data)

# Plotting the data
fig, ax = plt.subplots(figsize=(16, 8))

# Colors for the bars
colors_max = '#87CEFA'  # Light blue for max expression
colors_min = '#FFB6C1'  # Light pink for min expression

# Bar plot for max and min expression values
index = np.arange(len(normalized_df['Species']))
bar_width = 0.35

# Plotting max and min expression with lighter colors
bars_max = ax.bar(index, normalized_df['Max Expression Value'], bar_width, label='Max Expression', color=colors_max)
bars_min = ax.bar(index + bar_width, normalized_df['Min Expression Value'], bar_width, label='Min Expression',
                  color=colors_min)

# Adjust y-axis to extend to 4 for better annotation visibility
ax.set_ylim(0, 4)

# Adding labels and titles
ax.set_xlabel('Species', fontsize=14, fontweight='bold')
ax.set_ylabel('$\mathbf{\it{MIZ1}}$  gene Expression', fontsize=14, fontweight='bold')
#ax.set_title('Max and Min Expression Regions Across Species')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(normalized_df['Species'], rotation=50, ha="right")
ax.legend()

# Annotate bars with the region names
for i in range(len(normalized_df)):
    # Annotate max expression with bold text
    ax.text(i - bar_width / 2, normalized_df['Max Expression Value'][i] + 0.1,
            normalized_df['Max Expression Region'][i], ha='center', va='bottom', fontsize=10, color='blue',
            fontweight='bold')

    # Annotate min expression with bold text
    ax.text(i + bar_width / 2, normalized_df['Min Expression Value'][i] + 0.1,
            normalized_df['Min Expression Region'][i], ha='center', va='bottom', fontsize=10, color='red',
            fontweight='bold')

plt.tight_layout()
plt.show()

# Display the normalized data with regions for max and min expression
normalized_df[['Species', 'Max Expression Region', 'Min Expression Region']]

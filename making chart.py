import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Buy', 'Store', 'Reading label', 'Spraying Material', 'Protective clothing', 
             'Dispose of empty containers', 'Food or others consumed', 'Washing hand and equipment']
subcategories = [
    ['Local markets', 'Dealer', 'Company', 'Other Farmers'],  # Buy
    ['House', 'Spcial place'],  # Store
    ['Never', 'Yes'],  # Reading label
    ['Spray', 'Hand spreading', 'Both'],  # Spraying Material
    ['Yes', 'No'],  # Protective clothing
    ['Thrown Away', 'Burning', 'Bring it home.'],  # Fate of empty containers
    ['Smoking', 'Drinking', 'Eating', 'Nothing'],  # Food or others consumed
    ['Field', 'House yard', 'Other place']  # Washing hand and equipment
]

# Values corresponding to each category
values = [
    [82, 5.5, 10, 2.5],  # Buy
    [88.5, 11.5],  # Store
    [82.3, 17.7],  # Reading label
    [78, 15,7],  # Spraying Material
    [15.8, 84.2],  # Protective clothing
    [78.5, 10, 11.5],  # Fate of empty containers
    [68, 13.3, 6, 12.7],  # Food or others consumed
    [78, 16, 6]  # Washing hand and equipment
]

# Set up the figure and the axis
fig, ax = plt.subplots(figsize=(10, 6))

# X-axis positions for the bar chart
x_pos = np.arange(len(categories))

# Plot the bars for each category and subcategory
for i, category in enumerate(categories):
    total_bars = len(subcategories[i])
    for j in range(total_bars):
        bar = ax.bar(i + j / total_bars, values[i][j], width=1 / total_bars, label=subcategories[i][j])
        
        # Annotate bars with their values (display numbers on top of bars)
        for rect in bar:
            height = rect.get_height()
            ax.annotate(f'{height}',  # The text to show (the height)
                        xy=(rect.get_x() + rect.get_width() / 2, height),  # Position of the text
                        xytext=(0, 3),  # Offset the text slightly
                        textcoords="offset points",  # Use offset points as coordinates
                        ha='center', va='bottom', fontsize=8)

# Customize the chart
ax.set_xticks(x_pos)
ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax.set_ylim(0, 120)
ax.set_ylabel('Percentage')

# Show legend outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Subcategories")

# Show the plot
plt.tight_layout()
plt.show()

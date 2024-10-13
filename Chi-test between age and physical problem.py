import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

# Create the data as a pandas DataFrame
data = {
    'Age Group': ['20-30', '31-40', '41-50', '51-60', '61-70'],
    'Physical Problems (Yes)': [65, 109, 74, 29, 6],
    'Physical Problems (No)': [26, 43, 29, 15, 4]
}

df = pd.DataFrame(data)

# Adding a total row to the DataFrame
df.loc['Total'] = df[['Physical Problems (Yes)', 'Physical Problems (No)']].sum()

# Display the DataFrame
print("Data Table:")
print(df)

# Prepare the contingency table for the Chi-Square test
contingency_table = df[['Physical Problems (Yes)', 'Physical Problems (No)']].iloc[:-1].values  # Exclude total row

# Perform the Chi-Square test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Print the results
print("\nChi-Square Test Results:")
print(f"Chi-Squared Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("\nExpected Frequencies:")
print(expected)

# Interpret the p-value
alpha = 0.05
if p_value < alpha:
    print("\nReject the null hypothesis: There is a significant association between age group and physical problems.")
else:
    print("\nFail to reject the null hypothesis: There is no significant association between age group and physical problems.")

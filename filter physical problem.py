# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load your dataset (assuming it's a CSV file named 'farmer_data.csv')
# Ensure that your file has columns like 'Age' and 'Physical Problem'
data = pd.read_csv('testx.csv')

# Step 3: Define the age ranges you want to analyze
age_ranges = {
    '20-30': (20, 30),
    '31-40': (31, 40),
    '41-50': (41, 50),
    '51-60': (51, 60),
    '61-90': (61, 90)
}

# Step 4: Initialize a dictionary to store the results
results = []

# Step 5: Iterate through each age range, filter data, and count physical problems
for age_group, (age_min, age_max) in age_ranges.items():
    # Filter the data for the current age range
    age_filtered = data[(data['Age'] >= age_min) & (data['Age'] <= age_max)]
    
    # Count physical problems (Yes/No)
    problem_yes = age_filtered[age_filtered['Physical Problem'] == 'yes'].shape[0]
    problem_no = age_filtered[age_filtered['Physical Problem'] == 'no'].shape[0]
    
    # Append the results to the list
    results.append({
        'Age Group': age_group,
        'Physical Problem Yes': problem_yes,
        'Physical Problem No': problem_no
    })

# Step 6: Convert the results into a DataFrame for easy viewing
summary_df = pd.DataFrame(results)

# Step 7: Print the summary
print(summary_df)

# Step 8 (Optional): Save the results to a CSV file
summary_df.to_csv('physical_problems_by_age_group.csv', index=False)

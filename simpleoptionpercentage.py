import pandas as pd

# Load the Excel file
file_path = 'data1.xlsx'  # Change this to your file path
df = pd.read_excel(file_path)

# Specify the column that contains the questionnaire answers
question_column = 'Future generations will be affected by climate change'  # Replace with the actual column name

# Split multiple answers and count each option
def count_answers(column):
    counts = {}
    for answers in column.dropna():  # Drop NaN values
        for answer in str(answers).split(','):  # Assuming answers are comma-separated
            answer = answer.strip()  # Remove leading/trailing whitespace
            if answer in counts:
                counts[answer] += 1
            else:
                counts[answer] = 1
    return counts

# Count the answers
answer_counts = count_answers(df[question_column])

# Calculate the percentage
total_responses = sum(answer_counts.values())
answer_percentages = {answer: (count / total_responses) * 100 for answer, count in answer_counts.items()}

# Print the results
print("Answer Counts:", answer_counts)
print("Answer Percentages:", answer_percentages)

# Optional: Save the results to a new Excel file
result_df = pd.DataFrame(list(answer_percentages.items()), columns=['Answer', 'Percentage'])
result_df.to_excel('answer_percentages.xlsx', index=False)

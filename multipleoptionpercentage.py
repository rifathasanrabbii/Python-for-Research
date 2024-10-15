import pandas as pd

def calculate_percentage(file_path, question_column):
    # Load the data from the CSV file
    df = pd.read_csv("D:\Research Programming\My Research\sheet2.csv")

    # Split the answers in the specified question column
    answers = df[question_column].str.split(', ', expand=True).stack()
    
    # Count occurrences of each option
    counts = answers.value_counts()

    # Calculate total responses
    total_responses = len(df)

    # Calculate percentages
    percentages = (counts / total_responses) * 100

    # Create a DataFrame to display results
    results = pd.DataFrame({'Count': counts, 'Percentage': percentages}).reset_index()
    results.columns = ['Option', 'Count', 'Percentage']

    return results

if __name__ == "__main__":
    # Define the path to your CSV file and the column with the question
    file_path = 'D:\Research Programming\My Research\sheet2.csv'  # Update with your file path
    question_column = 'Students’ practices to prevent or reduce the impact of climate change?'  # Update with your question column name

    # Calculate and print percentages
    percentage_results = calculate_percentage(file_path, question_column)
    print(percentage_results)

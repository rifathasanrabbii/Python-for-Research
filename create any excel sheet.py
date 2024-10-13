import pandas as pd
import random

# Number of respondents
n = 400

know_about_toxicity = ['Yes']*83 + ['No']*317
random.shuffle(know_about_toxicity)

read_labels = ['Yes']*71 + ['No']*329
random.shuffle(read_labels)

harmful_to_crops = ['Yes']*49 + ['No']*299 + ['Don\'t Know']*52
random.shuffle(harmful_to_crops)

cause_human_illnesses = ['Yes']*182 + ['No']*218
random.shuffle(cause_human_illnesses)

environment_affected = ['Yes']*129 + ['No']*246 + ['Don\'t Know']*25
random.shuffle(environment_affected)

know_effects_on_body = ['Yes']*117 + ['No']*283
random.shuffle(know_effects_on_body)

received_training = ['Yes']*97 + ['No']*303
random.shuffle(received_training)

data = {
    'Know About Toxicity': know_about_toxicity,
    'Read Labels Before Use': read_labels,
    'Harmful to Crops': harmful_to_crops,
    'Cause Human Illnesses': cause_human_illnesses,
    'Environment Affected': environment_affected,
    'Know Effects on Body': know_effects_on_body,
    'Received Training on Safe Use': received_training
}    

df = pd.DataFrame(data)

# Save to Excel file on your PC
file_path = 'finalxx.xlsx'  # You can change the path if necessary
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")

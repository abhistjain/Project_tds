import pandas as pd

# Load the users data from the CSV file
users_df = pd.read_csv('users.csv')

# Total number of users
total_users = len(users_df)

# Filter hireable and non-hireable users
hireable_users = users_df[users_df['hireable'] == True]
non_hireable_users = users_df[users_df['hireable'].isna() | (users_df['hireable'] == False)]

# Calculate the fraction of users with email in both groups
fraction_hireable_with_email = hireable_users['email'].notna().mean()
fraction_non_hireable_with_email = non_hireable_users['email'].notna().mean()

# Calculate the difference
difference = fraction_hireable_with_email - fraction_non_hireable_with_email

# Print the result rounded to three decimal places
print(f'Difference in fraction of users with email: {difference:.3f}')
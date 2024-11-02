import pandas as pd

# Load the users data from the CSV file
users_df = pd.read_csv('users.csv')

# Filter hireable and non-hireable users
hireable_users = users_df[users_df['hireable'] == True]
non_hireable_users = users_df[users_df['hireable'].isna() | (users_df['hireable'] == False)]

# Calculate average following for both groups
average_hireable_following = hireable_users['following'].mean()
average_non_hireable_following = non_hireable_users['following'].mean()

# Calculate the difference
difference = average_hireable_following - average_non_hireable_following

# Print the result rounded to three decimal places
print(f'Difference in average following (hireable - non-hireable): {difference:.3f}')

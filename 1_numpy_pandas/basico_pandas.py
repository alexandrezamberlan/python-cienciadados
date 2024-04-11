import pandas as pd

# create two sample DF
data1 = {'ID': [1, 2, 3, 4, 5, 6],
         'Name': ['Ana', 'João', 'Ricardo','Alex', 'Bernardo', 'Carlos']}
data2 = {'ID': [1, 2, 3, 4, 5, 6],
         'Age': [25, 30, 35, 49, 21, 12]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# merge the DF using a common column (ID)
merged_df = pd.merge(df1, df2, on='ID', how='inner')

print("\nMerged DataFrame:")
print(merged_df)

# calculate the mean age of the merged DF
mean_age = merged_df['Age'].mean()
print(f"\nMean Age: {mean_age:.2f}")

# filter rows where Age is greater than the mean age
above_mean_age = merged_df[merged_df['Age'] > mean_age]
print("\nPeople above Mean Age:")
print(above_mean_age)

# sort the DF by Age in descending order
sorted_df = merged_df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age:")
print(sorted_df)

# reset the index of the DF after sorting
sorted_df.reset_index(drop=True, inplace=True)
print("\nDataFrame with Reset Index:")
print(sorted_df)

# create a new column 'Is_Adult' based on Age
sorted_df['Is_Adult'] = sorted_df['Age'] >= 18
print("\nDataFrame with New Column 'Is_Adult':")
print(sorted_df)

# group the data by 'Is_Adult' and calculate the mean of 'Age' for each group
age_groups = sorted_df.groupby('Is_Adult')['Age'].mean()
print("\nMean Age by 'Is_Adult' Group:")
print(age_groups)
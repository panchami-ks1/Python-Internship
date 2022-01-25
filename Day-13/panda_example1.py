import pandas as pd

x = pd.read_csv('cities.csv')
# Removing empty rows
new_data = x.dropna(inplace=True)

# Replacing empty rows
new_data = x.fillna(100)
print(x.info())
# Median,mean and mode
approx_median_value = x['LonD'].median()
approx_mean_value = x['LonD'].mean()
approx_mode_value = x['LonD'].mode()
# Replacing empty cells with column names
new_data = x['LonD'].fillna(approx_median_value, inplace=True)
# Removing Duplicate value
x.drop_duplicate(inplace=True)
print(x.info)








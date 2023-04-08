import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(
    filepath_or_buffer="http://lib.stat.cmu.edu/datasets/boston",
    delim_whitespace=True,
    skiprows=21,
    header=None,
)

columns = [
    'CRIM',
    'ZN',
    'INDUS',
    'CHAS',
    'NOX',
    'RM',
    'AGE',
    'DIS',
    'RAD',
    'TAX',
    'PTRATIO',
    'B',
    'LSTAT',
    'MEDV',
]

#Flatten all the values into a single long list and remove the nulls
values_w_nulls = df.values.flatten()
all_values = values_w_nulls[~np.isnan(values_w_nulls)]

#Reshape the values to have 14 columns and make a new df out of them
df = pd.DataFrame(
    data = all_values.reshape(-1, len(columns)),
    columns = columns,
)

print(df.describe())

# plt.scatter(df.CRIM, df.MEDV)
# plt.xlabel("Per capita crime rate by town (CRIM)")
# plt.ylabel("Housing Price")
# plt.title("Relationship between crime and median Price")

# There is a clear positive relationship between the number of rooms and the price of the house.
# plt.scatter(df.RM, df.MEDV)
# plt.xlabel("Number of rooms in the house")
# plt.ylabel("Housing Price")
# plt.title("Relationship between number of rooms and median Price")

# There is a slight negative ralationship between the pupil to teacher ratio and the price.
# plt.scatter(df.PTRATIO, df.MEDV)
# plt.xlabel("Pupil teacher ratio by town")
# plt.ylabel("Housing Price")
# plt.title("Relationship between PT-Ratio and median Price")

# There si a negative correlation between tax rate and median price.
plt.scatter(df.TAX, df.MEDV)
plt.xlabel("Tax rate")
plt.ylabel("Housing Price")
plt.title("Relationship between tax rate and median Price")

plt.show()

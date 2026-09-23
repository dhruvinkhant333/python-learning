
print("""
# ---------------------------------------------------------------------------- #
#                               one-hot encoding                               #
# ---------------------------------------------------------------------------- #
""")
'''
EXAMPLE: 
there is a student with the following values:
Edward Remirez, Male, 28 years, Bachelors Degree
We can convert the gender column to the set of three values:
Edward Remirez, 0, 1, 0, 28 years, Bachelors Degree

GenderIs Female?Is Male?Is Other?
Female   1         0       0
Male     0         1       0
Other    0         0       1
'''


import pandas as pd 
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame([["Edward Remirez", "Male", 28, "Bachelors"], ["Arnav Sharma", "Male", 23, "Masters"], ["Sophia smith", "Female", 19, "High School"]] , 
                  columns=['Name', 'Gender', 'Age', 'Degree'])
print(df)

encoder_for_gender = OneHotEncoder().fit(df[['Gender']])

print(encoder_for_gender.categories_)

gender_value = encoder_for_gender.transform(df[['Gender']])

print(gender_value.toarray())

df[['Gender_F', 'Gender_M']] = gender_value.toarray()

print(df)

print("""
# ---------------------------------------------------------------------------- #
#                        Transforming Ordinal Attributes                       #
# ---------------------------------------------------------------------------- #
""")

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# df = pd.DataFrame([
#     ["Edward Remirez", "Male", 28, "Bachelors"],
#     ["Arnav Sharma", "Male", 23, "Masters"],
#     ["Sophia Smith", "Female", 19, "High School"]
# ], columns=["Name", "Gender", "Age", "Degree"])

# print(df)

# Create the Encoder
encoder = OrdinalEncoder()

#Give the Degree Data to the Encoder
df[["Degree"]]

#fit() — Learn the Categories
encoder.fit(df[["Degree"]])
print(encoder.categories_)

# Tell the Encoder the Correct Order
encoder = OrdinalEncoder(
    categories=[[
        "High School",
        "Bachelors",
        "Masters",
        "Doctoral"
    ]]
)

# Now fit_transform()
df["Degree_encoded"] = encoder.fit_transform(df[["Degree"]])

#now the DataFrame look like : 
print(df)

# The columns for Gender and Degree can now be removed. We can also remove the column for
# Name as we believe it to have minimal information that any model should capture.
df.drop(columns=['Gender', 'Degree'], inplace=True)
print(df)


print("""
# ---------------------------------------------------------------------------- #
#                                 Normalization                                #
# ---------------------------------------------------------------------------- #
""")

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# This section is about scaling numerical features.

# Age            → 19, 23, 28
# Gender_F       → 0, 1
# Gender_M       → 0, 1
# Degree_encoded → 0, 1, 2

# Age has much larger numbers than the other columns. Scaling brings the features into a comparable numerical range.

df = pd.DataFrame({'Age': {0: 28, 1: 23, 2:19},
                   'Gender_F': {0: 0.0, 1: 0.0, 2:1.0},
                   'Gender_M': {0: 0.0, 1:1.0, 2: 0.0},
                   'Degree_encoded': {0: 0.0, 1: 2.0, 2: 1.0}})


# By use of scalling We're changing the numerical representation, not the actual information.

print("# ------------------------------ Min-Max Scaling ----------------------------- #")
scaler = MinMaxScaler()

# fir age with minmaxscaler so this can remamber which value is max and which one is min ....
scaler.fit(df[['Age']])

# Transform the data ( remamber not changing )
df['Age'] = scaler.transform(df[['Age']])

print(df)

print("# ----------------------------- Standard Scaling ----------------------------- #")

scaler = StandardScaler()

#fit 
scaler.fit(df[['Age']])

# Transform 
df['Age'] = scaler.transform(df['Age'])

print(df)

# You can view the parameters of the scaler using
print(scaler.mean_)
print(scaler.scale_)
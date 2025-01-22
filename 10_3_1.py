import pandas as pd
df = pd.DataFrame({
    "Name": ["Suryansh", "Avanish", None],
    "Age": [18, 17, None]
})
print(df)
df.dropna(inplace=True)
print(df)  # Rows with missing data are gone!

df.fillna(df.mean(), inplace=True)
print(df)  # Missing 'Age' values are replaced with the mean!

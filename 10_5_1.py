import pandas as pd
df = pd.DataFrame({
     "Name": ["Suryanhsk", "Avanish"],
    "Age": [18, 17]
})
print(df['Age'].mean())  # Mean
print(df['Age'].median())  # Median
print(df['Age'].mode())  # Mode

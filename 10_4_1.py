import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
     "Name": ["Suryanhsk", "Avanish"],
    "Age": [18, 17]
})
df['Age'].hist()
plt.show()

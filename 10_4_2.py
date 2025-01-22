import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
     "Name": ["Suryanhsk", "Avanish"],
    "Age": [18, 17]
})

sns.boxplot(x="Age", data=df)
plt.show()

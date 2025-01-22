import pandas as pd

df = pd.DataFrame({
    "Ad_Spend": [1000, 1500, 2000, 2500, 3000],  
    "Sales": [10, 15, 20, 25, 30] 
})

print(df.corr())

'''
1 means perfect positive correlation
 (as one goes up, the other goes up).

 -1 means perfect negative correlation
 (as one goes up, the other goes down).

 0 means no correlation.
'''
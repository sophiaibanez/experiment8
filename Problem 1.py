import pandas as pd
    
cars = pd.read_csv('cars.csv')
df = cars.head().append(cars.tail())
print(df)


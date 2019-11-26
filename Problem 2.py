import pandas as pd

cars = pd.read_csv('cars.csv')
y = df.iloc[0:5,0:12:2]
print (y)

z = df.loc[df['Model'] == 'Mazda RX4']
print (z)

a = df.loc[df['Model'] == 'Camaro Z28', ['Model','cyl']]
print (a)

b = df.loc[df['Model'] == 'Mazda RX4 Wag', ['Model','cyl','gear']]
c = df.loc[df['Model'] == 'Ford Pantera L', ['Model','cyl','gear']]
d = df.loc[df['Model'] == 'Honda Civic', ['Model','cyl','gear']]
print(b,d,a)
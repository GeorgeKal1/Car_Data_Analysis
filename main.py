import pandas as pd



df=pd.read_csv('carData.csv')

toyotas = df[df['Make'] == 'Toyota'].value_counts()
print(toyotas)
import pandas as pd

#reading a csv, parsing
df = pd.read_csv('personal.csv')
print(df)

data = {
    'name': ['Niyas', 'Thoufiq', 'Aakash', 'Farid'],'number': ['38210983','2831903', '382901', '29310381'], 'street': ['chine', 'maine', 'kayne', 'wayne'], 'city': ['chennai', 'chennai', 'datae', 'vellore'], 'state': ['tamilnadu', 'tamilnadu', 'mp', 'tamilnadu'], 'pin':['12', '123', '13', '124']
}

#converting a dictionary to write to a csv.
df = pd.DataFrame(data, columns=['name', 'number', 'street','city', 'state', 'pin'])

export_csv = df.to_csv(r'personal1.csv', index=None)

#filtering the csv data by searching for "tamilnadu" in state.
a = df[df['state'] == "tamilnadu"]
print(a)

#creating a new dataframe/csv file with the counts of city and state houses.
df1 = pd.read_csv('personal1.csv')
df3 = df1.groupby(['city', 'state'])

print(df3.count())
export_csv = df3.count().to_csv(r'personal2.csv', index=None)


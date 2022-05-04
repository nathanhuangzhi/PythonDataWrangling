import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
d = {'col1': ser1, 'col2': ser2}
df = pd.DataFrame(d)
# print(df)


ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.index.name = 'alpha'
ser.name = 'alpha'
# print(ser)

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# print(ser1[~ser1.isin(ser2)])

s1 = ser1[~ser1.isin(ser2)]
s2 = ser2[~ser2.isin(ser1)]
s3 = s1.append(s2)
# print(s3)


ser = pd.Series(np.random.normal(10, 5, 25))
# print(ser.median())
# print(ser.min())
# print(np.percentile(ser, q=[0,25,50,75,100]))

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
s = {'col':ser}
df = pd.DataFrame(s)
# print(df.groupby(by='col')['col'].count())

ser = pd.Series(np.random.randint(1, 5, [12]))
s = {'col':ser}
df = pd.DataFrame(s)
df_ordered = df.groupby(by='col')['col'].count().sort_values(ascending=False)
df_top2 = df_ordered.nlargest(2)
df['col2'] = df['col']
df.loc[df['col'].isin(df_top2),'col2'] = 'Other'
# print(df)


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url,sep = '\t')
c = chipo.groupby('item_name').sum('quantity').sort_values('quantity',ascending=False)
#print(c.head(1))

cd = chipo.groupby('choice_description').sum('quantity').sort_values('quantity',ascending=False)
#print(cd.head(1))

ci = chipo['item_name'].nunique()

floatize = lambda x: float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(floatize)
# print(chipo.info())

chipo['sales'] = chipo['item_price'] * chipo['quantity']
# print(chipo['sales'].sum())

ca = chipo.groupby('order_id').sum('sales')
# print(ca['sales'].mean())

# print(chipo['item_name'].nunique())


users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',
                      sep='|', index_col='user_id')

# print(users.info())

# print(dir(users))

# print(users['age'].nsmallest(5))

minoccur = users.groupby('age')['age'].count().sort_values(ascending=True)
# print(minoccur[minoccur==1])

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep = '\t')

dollarize = lambda x: float(x[1:-1])
chipo['item_price'] = chipo['item_price'].apply(dollarize)
# print(chipo[chipo['item_price']>10]['item_name'])

# print(chipo.groupby('item_name')['item_name','item_price'].mean('item_price'))

# print(chipo[['item_name','item_price']])

# print(chipo.sort_values('item_name'))

# print(chipo.sort_values('item_price',ascending=False).head(1))

# print(chipo[chipo['item_name']=='Veggie Salad Bowl']['order_id'].count())

# print(chipo[(chipo['item_name']=='Canned Soda') & (chipo['quantity']>1) ]['order_id'].count())

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)

capitalizer = lambda x: x.capitalize()
# print(df['Mjob'].apply(capitalizer))

def majority(x):
   if x>17:
       return True
   else:
       return False

df['legal_drinker'] = df['age'].apply(majority)
# print(df)
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)

crime['Year'] = pd.to_datetime(crime['Year'])


cars1 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
cars2 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")


raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data_1 = pd.DataFrame(raw_data_1)
data_2 = pd.DataFrame(raw_data_2)
data_3 = pd.DataFrame(raw_data_3)

all_data = pd.concat([data_1,data_2],axis=0)
# all_data = pd.concat([data_1,data_2],axis=1)
# print(all_data)

merge_data = pd.merge(all_data,data_3,on = 'subject_id')
# print(merge_data)
# print(pd.merge(data_1,data_2,on = 'subject_id', how= 'inner'))
#print(pd.merge(data_1,data_2,on = 'subject_id', how= 'left'))

data_4 = data_1.rename(columns = {'subject_id': 'bedrs'})
# print(data_4)

# baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')

# print(baby_names.groupby('Name')['Count'].sum().sort_values(ascending=False).head())

# print(baby_names['Name'].nunique())

data_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data'
data = pd.read_csv(data_url, sep = "\s+", parse_dates = [[0,1,2]])

dateconvert = lambda x : pd.to_datetime(x,format='%Y')
data['Year'] = data['Yr_Mo_Dy'].apply(dateconvert)
print(data['Year'].unique())
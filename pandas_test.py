import numpy as np
import pandas as pd
df = pd.DataFrame(np.array((['mouse',1, 6, 3], ['rabbit',4, 5, 6])),

                  columns=['class','one', 'two', 'three'])
# print(df[df['three'] == df['three'].max()])

# print(df[df['class']== 'mouse'])

print(df.sort_values(by=['two','three'],ascending=True))



Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

Car_Price = pd.DataFrame(Car_Price)
car_Horsepower = pd.DataFrame(car_Horsepower)

df_new = Car_Price.merge(car_Horsepower,on = 'Company',how = 'left')
print(df_new)
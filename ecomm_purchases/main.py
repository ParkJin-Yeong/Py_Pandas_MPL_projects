import pandas as pd

data = pd.read_csv("purchases.csv")

# Display top 10 rows of dataframe

#print(data.head(10))
#print(data.iloc(0))

# Display last 10 rows of dataframe

#print(data.tail(10))

#Check Datatype of Each Column

#print(data.dtypes)

# Check Null Values in the Dataframe

#print(data.isnull())
#print(data.isnull().sum())

#How many rows and columns are there in our dataframe?

#print(data.shape)
#print(len(data.columns))
#print(len(data))
#print(data.info())

#Highest and Lowest Purchase Prices

#print(data['Purchase Price'].max())
#print(data['Purchase Price'].min())
#print(max(data['Purchase Price']))
#print(min(data['Purchase Price']))

#Average Purchase Price

#print(data['Purchase Price'].mean())
# print(data['Purchase Price'].sum()/len(data))
# print(sum(data['Purchase Price'])/data.shape[0])

#How many people speak French 'fr" as their language?

#print(sum(data['Language']=='fr'))
#print((data['Language']=='fr').sum())
#print(len(list(l for l in data['Language'] if l == "fr")))

#print(data[data['Language']=='fr'].count())




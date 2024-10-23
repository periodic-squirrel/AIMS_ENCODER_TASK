import pandas as pd
import numpy as np

#datalist is a list of data to be encoded

print("********ORDINAL ENCODER********")

def ordinal_encoder(datalist):
    encoded=[]          #WILL STORE ENCODED VALUES
    data_value=[]       #WILL STORE INPUT UNIQUE VALUES 
    encoded_value=0     #WILL KEEP A TRACK OF ENCODED VALUES
    for i in datalist:
        if i not in data_value:
            data_value.append(i)
            encoded.append(encoded_value)
            encoded_value+=1
    print("INPUT VALUES:")
    print(data_value)
    print("ENCODED VALUES:")
    print(encoded)
ordinal_encoder(["AVERAGE","ABOVE AVERAGE","BELOW AVERAGE","GOOD","AVERAGE","GOOD","AVERAGE"])

print("********ONE HOT ENCODER********")
#IT TAKES TWO ARGUMENTS:THE DATAFRAME AND THE COLUMN TO PERFORM ON
def one_hot_encoder(df,col):
    name_of_cols=df[col].unique()
    for i in name_of_cols:
        df[i]=0
    for i in name_of_cols:
        df.loc[df[col]==i, i] += 1
    return df
data = {
    'Product': ['Shirt', 'Pants', 'Hat', 'Shirt', 'Hat', 'Pants'],
    'Colour': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Green'],
    'Type': ['Clothing', 'Clothing', 'Accessory', 'Clothing', 'Accessory', 'Clothing']
}

df = pd.DataFrame(data)
out=one_hot_encoder(df,'Colour')
print(out.head())
    
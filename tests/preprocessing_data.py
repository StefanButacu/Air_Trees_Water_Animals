import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

DATA_PATH = '../data/Environment_Temperature_change_E_All_Data_NOFLAG.csv'

data_frame = pd.read_csv(DATA_PATH, encoding='cp1252')
#print(data_frame.shape)
#print(data_frame.head(10))

scaling_columns = ['Y' + str(i) for i in range(1961,2020)]

# print(data_frame[scaling_columns])
# data_frame[scaling_columns] = StandardScaler().fit_transform(data_frame[scaling_columns].values)
# print(data_frame[scaling_columns])

area_code_column = ['Area Code']

print(data_frame[area_code_column])
print(LabelEncoder().fit_transform(data_frame[area_code_column].values))
print(data_frame[area_code_column])
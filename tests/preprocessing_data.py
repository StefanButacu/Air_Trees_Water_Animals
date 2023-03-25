import pandas as pd
from sklearn.preprocessing import MinMaxScaler

DATA_PATH = 'data/Environment_Temperature_change_E_All_Data_NOFLAG.csv'

data_frame = pd.read_csv(DATA_PATH, encoding='cp1252')
print(data_frame.shape)
print(data_frame.head(10))

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OrdinalEncoder

import pickle

df = pd.read_csv(r"C:\Datasets\used_car_price_dataset_extended.csv")
print(df.columns)

#print(df.isnull().sum())

df['service_history'] = df['service_history'].fillna('No_history')

oe = OrdinalEncoder()
df[['fuel_type', 'brand','transmission','color','service_history','insurance_valid']] = oe.fit_transform(df[['fuel_type', 'brand','transmission','color','service_history','insurance_valid']])

x = df[['make_year', 'mileage_kmpl', 'engine_cc', 'fuel_type', 'owner_count', 'brand', 'transmission', 'color', 'service_history',
       'accidents_reported', 'insurance_valid']]
y = df['price_usd']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(mse, mae, r2)

fh = open('model.pkl', 'wb')
pickle.dump(model, fh)

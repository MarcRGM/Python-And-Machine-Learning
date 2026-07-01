import numpy as np # For generating data
from sklearn.linear_model import LinearRegression # For creating and training the model
from sklearn.metrics import mean_absolute_error # For making predictions and measuring error
from sklearn.model_selection import train_test_split # For training

model = LinearRegression()

house_sizes = np.random.uniform(30.0, 200.0, 50) # low (inclusive), high (exclusive), count
noise = np.random.normal(0, 20000, 50) # mean, std, count
price = house_sizes * 1500 + 20000 + noise
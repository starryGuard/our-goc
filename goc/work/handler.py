import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.python.data import Dataset
import sklearn.metrics as metrics
import math
from matplotlib import pyplot as plt

sku_info_data = pd.read_csv("../data/sku_info.csv", sep=",")
sku_attr_data = pd.read_csv("../data/sku_attr.csv", sep=",")
sku_sales_data = pd.read_csv("../data/sku_sales.csv", sep=",")
print(sku_sales_data.sample(10))
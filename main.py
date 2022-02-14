import pandas as pd

data_set = None # Initialises the variable

try:
  data_set = pd.read_csv("dataset01.csv") # Loads the data set 
except:
  pass

def show_info():
  print(data_set.head()) # Shows the first 5 rows of the data set
  print(data_set.head(12)) # Shows the first 12 rows of the data set
  print(data_set.tail()) # Returns the last 5 rows of the data set
  print(data_set.info) # Gets information about the dataset this could be
  # how large the file is, how many columns and the column data type.

show_info()
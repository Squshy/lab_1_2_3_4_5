import os
import pandas as pd
import numpy as np
from itertools import combinations

# Reads a test file and returns its data in an array
def GetItemsetFromFile(file):
  return np.asarray([i.strip().split() for i in open(file, 'r').readlines()])

# Takes an array of support values and the data values and appends them together
def CreateSupportList(data, support):
  i = 0
  new_list = []
  for clump in data:
    current_list = []
    for item in clump:
      current_list.append(item)
    current_list.append(support[i])
    new_list.append(current_list)
    i+=1
  return new_list

# Saves a Pandas DataFrame to an html file
def SaveDataFrameToHTMLFile(df, filename):
  html = df.to_html()
  filepath = "./report/table_files/" + filename + ".html"
  try:
    os.remove(filepath)
  except OSError:
    pass
  file = open(filepath, 'a')
  file.write(html)
  file.close()

# Get subsets of data
def rSubset(data, r):
  return list(combinations(data, r))

# Gets x % of data from the data passed
# If you pass 0.2, you get 20% of the data returned starting from the beginning of the data
def GetSubsectionOfData(data, percent):
  data_len = len(data)
  amount_of_data = round(data_len * percent)
  print("%d%% of %d is %d" % ((percent * 100), data_len, len(data[:amount_of_data])))
  return data[:amount_of_data]

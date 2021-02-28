import numpy as np
import math
from helper import rSubset, GetFrequentItems

# Hash function for mapping data to buckets
def HashFunction(pair, data_size):
  return math.floor((int(pair[0]) * int(pair[1])) % (data_size * .3))

# First pass of data
def PassOne(data, support):
  occurences = {}   # Save the number of times an item has occured in the data 
  hash_table = {}   # Hash table to save data of pairs hashed to a bucket 
  i = 0
  # Loop through every line in the data
  for line in data:
    if i % 50000 == 0:
      print("Reading line %d of %d" % (i, len(data)))
    # Loop through every item in that line
    for item in line:
      # If the item is not currently accounted for, set its counter to 1
      if item not in occurences:
        occurences[item] = 1
      # If it is accoutned for, add one to its counter
      else:
        occurences[item] += 1
    i +=1
    #
    # Everything till now was same as Apriori
    # NEW TO PCY
    #
    pairs_of_items = rSubset(line, 2)  # Want to get pairs of items
    for pair in pairs_of_items:
      # Hash the pair to a bucket
      key = HashFunction(pair, len(data))
      if key not in hash_table:
        hash_table[key] = 1
      else: 
        hash_table[key] += 1

  # Return a list of frequent items
  return GetFrequentItems(occurences, support * len(data))
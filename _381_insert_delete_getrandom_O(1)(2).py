"""
381. Insert Delete GetRandom O(1) - Duplicates allowed

    Total Accepted: 37
    Total Submissions: 94
    Difficulty: Medium

Design a data structure that supports all following operations in average O(1) time.
Note: Duplicate elements are allowed.

    insert(val): Inserts an item val to the collection.
    remove(val): Removes an item val from the collection if present.
    getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""
import random

class RandomizedCollection(object):
    def __init__(self):
        self.collection = {}        # key = item stored in array, value = appearances
        self.data = set()           # store all items in the array

    def insert(self, val):
        if val not in self.collection.keys():
            self.collection[val] = 1
            self.data.add((val, 1))
            return True
        else:
            self.collection[val] += 1
            self.data.add((val, self.collection[val]))
            return False

    def remove(self, val):
        # if exist => remove it from dictionary and set
        # if appearances == 0 => remove from the dictionary

        if val in self.collection.keys():
            self.data.remove((val, self.collection[val]))
            self.collection[val] -= 1
            if self.collection[val] == 0: del self.collection[val]
            return True
        else:
            return False

    def getRandom(self):
        return random.sample(self.data, 1)[0][0]
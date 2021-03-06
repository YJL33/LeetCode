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
        """
        Initialize your data structure here.
        """
        self.collection = {}        # key = item stored in array, value = set of index
        self.array = []             # store all items in the array

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        index = len(self.array)
        self.array += val,

        if val not in self.collection.keys():
            self.collection[val] = set([index])
            return True
        else:
            self.collection[val].add(index)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        # if exist => remove it from dictionary and list,
        # swap last element and val position in the array, and delete the last one
        if not self.array or val not in self.collection.keys():
            return False

        else:
            last = self.array[-1]                           # the other element
            i_last = len(self.array)-1                      # index of last position
            i_val = self.collection[val].pop()              # index of val position
            self.array[i_val] = self.array[i_last]          # update the array
            self.array.pop()

            self.collection[last].add(i_val)                # update the dict
            self.collection[last].remove(i_last)

            if len(self.collection[val]) == 0: del self.collection[val]         # remove empty set
            
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if len(self.array) == 0: return -1
        else: return self.array[random.randint(0, len(self.array)-1)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
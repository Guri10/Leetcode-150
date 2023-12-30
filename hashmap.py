'''

380. Insert Delete GetRandom O(1)
Difficulty: Medium
URL: https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.
    1. insert(val): Inserts an item val to the set if not already present.
    2. remove(val): Removes an item val from the set if present.
    3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
'''



import random

class RandomizedSet(object):

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val in self.numMap
        if res:
            indx = self.numMap[val]
            self.numList[indx] = self.numList[-1]
            self.numMap[self.numList[-1]] = indx
            self.numList.pop()
            del self.numMap[val]
        return res

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numList)
        
# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())

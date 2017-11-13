# -*- coding: utf-8 -*-
class Hashtable:    
    def __init__(self, dict={}):
        self._tableSize = max(1, len(dict) - 1)
        self._buckets = [ [] for i in range(self._tableSize) ]  
        self._data = [ [] for i in range(self._tableSize) ]   
        for key, value in dict.iteritems():
            self.__setitem__(key, value)

    def __getitem__(self, key):
        index = hash(key) % self._tableSize
        bucket_size = len(self._buckets[index])
        for x in range(bucket_size):
            if self._buckets[index][x] == key:            
                return self._data[index][x]

    def __setitem__(self, key, value):
        index = hash(key) % self._tableSize
        bucket_size = len(self._buckets[index])
        if bucket_size == 0:
            self._buckets[index] = [key]
            self._data[index] = [value]
        else:
            for x in range(bucket_size):
                if self._buckets[index][x] == key:
                    self._data[index][x] = value
                    return
            self._buckets[index].append(key)
            self._data[index].append(value)
         
    def __delitem__(self, key):
        index = hash(key)% self._tableSize
        bucket_size = len(self._bucekts[index])
        value = self.__getitem__(key)
        for k in range(bucket_size):
            if self._buckets[index][k] == key:
                self._buckets[index].remove(key)
                self._data[index].remove(value)
                return
               
    def keys(self):
        keys = []
        for x in range(self._tableSize):
            for chain in self._buckets[x]:
                keys.append(chain)
        return keys

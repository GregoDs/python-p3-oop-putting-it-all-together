#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

#Shoe in shoe.py prints "size must be an integer" if size is not an integer.
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if (isinstance(size,int)):
            self._size  = size
        else:
            print("size must be an integer")

    size = property(get_size,set_size)
# Shoe in shoe.py says that the shoe has been repaired.
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    


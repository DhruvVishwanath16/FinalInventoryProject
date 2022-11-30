#Author: Grant Shaffer & Dhruv Vishwanath
#Assignment: Inventory class
#Date: 11/28/22
#Program Description: Inventory class for final project

class TransactionItem:
    
# Initializes the variables for the class
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__qty = 0
        self.__price = 0
    
# Accessor to get the id for the item
    def get_id(self):
        return self.__id
    
# Mutator for the id of the item
    def set_id(self, new_id):
        self.__id = new_id
    
# Accessor to get the name of the item
    def get_name(self):
        return self.__name
    
# Mutator for the name of the item
    def set_name(self, new_name):
        self.__name = new_name
        
# Accessor for the quantity of the item
    def get_qty(self):
        return self.__qty
    
# Mutator for the quantity of the item
    def set_qty(self, new_qty):
        if new_qty>0:
            self.__qty = new_qty
            
# Accessor for the price of the item
    def get_price(self):
        return self.__price
    
# Mutator for the price of the item
    def set_price(self, new_price):
        self.__price = new_price
        
# Function to calculate the cost of the item
    def calc_cost(self):
        cost = self.__qty*self.__cost
        return cost
# Returns the invoice for the item
    def __str__(self):
        transaction_cost = format(self.calc_cost, '.2f')
        string = str(self.__id) + ' ' + str(self.__name) + ' ' + str(self.__qty) + ' ' + str(self.__price) + ' $' + str(transaction_cost)
        return string
          

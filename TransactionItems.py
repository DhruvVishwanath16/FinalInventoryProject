#Author: Grant Shaffer & Dhruv Vishwanath
#Assignment: Inventory class
#Date: 11/28/22
#Program Description: Inventory class for final project

class TransactionItem:
    
# Initializes the variables for the class
    def __init__(self, new_id, new_name, new_qty, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__qty = new_qty
        self.__price = new_price
    
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
        transaction_cost = self.__qty * self.__price
        return transaction_cost
    
# Returns the invoice for the item
    def __str__(self):
        transaction_cost = self.calc_cost()
        string = format(self.__id,'2.0f') + '\t\t' + format(self.__name,'18') + '\t\t' + format(self.__qty,'8.0f') + '\t\t' + format(self.__price, '8.2f') + '\t' + ' $' + format((transaction_cost), '6.2f')
        return string

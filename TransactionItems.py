#Author: Grant Shaffer & Dhruv Vishwanath
#Assignment: TransactionItems class
#Date: 11/28/22
#Program Description: TransactionItems class for final project

class TransactionItem:
    
    
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__qty = 0
        self.__price = 0
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id
    
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name
        
    
    def get_qty(self):
        return self.__qty
    
    def set_qty(self, new_qty):
        if new_qty>0:
            self.__qty = new_qty
            
    
    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        self.__price = new_price
        
    
    def calc_cost(self):
        cost = self.__qty*self.__cost
        return cost
    
    def __str__(self):
        transaction_cost = format(self.calc_cost, '.2f')
        string = str(self.__id) + ' ' + str(self.__name) + ' ' + str(self.__qty) + ' ' + str(self.__price) + ' $' + str(transaction_cost)
        return string
        
        
    
    

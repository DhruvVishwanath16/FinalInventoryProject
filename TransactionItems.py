# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:08:18 2022

@author: echoe
"""

class TransactionItemClass:
    
    
    def __init__(self, new_id, new_name, new_stock, new_price):
        self.__id = new_id
        self.__name = new_name
        self.__quantity = new_stock
        self.__price = new_price
        
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 10:23:11 2021

@author: user
"""

class Birthday:
    
    def __init__(self, name, month, day):
        self.__name = name
        self.__month = month
        self.__day = day
        
    def getName(self):
        return self.__name
    
    def getMonth(self):
        return self.__month
    
    def getDay(self):
        return self.__day
    
    def __repr__( self ):
        return self.__name + " " + str(self.__month) + '/' + str(self.__day)
    
    def __lt__(self, other):
        return self.__name < other.__name
    
    def __eq__(self, other):
        if isinstance(other,Birthday):
            return  other.getName() == self.__name
        return False